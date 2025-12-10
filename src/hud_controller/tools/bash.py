import asyncio
import os
import re
import tempfile

from .base import CLIResult, ToolError, ToolResult


# =============================================================================
# Anti-cheat: Block git commands that could reveal the fix
# =============================================================================

# These commands could allow the agent to see commit history or the golden fix
BLOCKED_GIT_PATTERNS = [
    # History viewing commands
    r'\bgit\s+log\b',           # git log - shows commit history
    r'\bgit\s+reflog\b',        # git reflog - shows reference log
    r'\bgit\s+rev-list\b',      # git rev-list - lists commits
    
    # Commit inspection commands
    r'\bgit\s+show\s+[a-f0-9]', # git show <commit> - shows commit content
    r'\bgit\s+cat-file\b',      # git cat-file - low-level object access
    
    # Remote/fetch commands (shouldn't have remotes anyway, but block just in case)
    r'\bgit\s+fetch\b',
    r'\bgit\s+pull\b',
    r'\bgit\s+remote\b',
    
    # Branch/checkout to other commits
    r'\bgit\s+checkout\s+[a-f0-9]{7,}',  # git checkout <commit-hash>
    r'\bgit\s+switch\s+[a-f0-9]{7,}',    # git switch <commit-hash>
    
    # Accessing .git directory directly
    r'\.git/',                   # Any path containing .git/
    r'/evaluation/',             # Block access to evaluation directory
    r'/secure_git\b',            # Block access to secure git directory
]

# Commands that are ALLOWED (for agent's own work)
# git diff, git status, git add, git commit, git stash - all fine
# These help the agent track their own changes


def is_blocked_command(command: str) -> tuple[bool, str]:
    """
    Check if a command should be blocked for anti-cheat reasons.
    
    Returns:
        Tuple of (is_blocked, reason)
    """
    command_lower = command.lower()
    
    for pattern in BLOCKED_GIT_PATTERNS:
        if re.search(pattern, command_lower):
            return True, f"Command blocked: git history/remote commands are disabled to prevent cheating"
    
    return False, ""


class _BashSession:
    """A session of a bash shell."""

    _started: bool
    _process: asyncio.subprocess.Process

    command: str = "/bin/bash"
    _output_delay: float = 0.2  # seconds
    _timeout: float = 1500.0  # seconds (25 minutes)
    _sentinel: str = "<<exit>>"

    def __init__(self):
        self._started = False
        self._timed_out = False

    async def start(self):
        if self._started:
            await asyncio.sleep(0)
            return

        def demote():
            # This only runs in the child process
            os.setsid()
            os.setgid(1000)
            os.setuid(1000)

        self._process = await asyncio.create_subprocess_shell(
            self.command,
            preexec_fn=demote,
            shell=True,
            bufsize=0,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd="/home/ubuntu",
        )

        self._started = True

    def stop(self):
        """Terminate the bash shell."""
        if not self._started:
            raise ToolError("Session has not started.")
        if self._process.returncode is not None:
            return
        self._process.terminate()

    async def run(self, command: str):
        """Execute a command in the bash shell."""
        if not self._started:
            raise ToolError("Session has not started.")
        if self._process.returncode is not None:
            await asyncio.sleep(0)
            return ToolResult(
                system="tool must be restarted",
                error=f"bash has exited with returncode {self._process.returncode}",
            )
        if self._timed_out:
            raise ToolError(
                f"timed out: bash has not returned in {self._timeout} seconds and must be restarted.",
            )

        # =================================================================
        # Anti-cheat: Check if command should be blocked
        # =================================================================
        is_blocked, reason = is_blocked_command(command)
        if is_blocked:
            return CLIResult(
                output="",
                error=reason
            )

        # we know these are not None because we created the process with PIPEs
        assert self._process.stdin
        assert self._process.stdout
        assert self._process.stderr

        # send command to the process
        self._process.stdin.write(command.encode() + f"; echo '{self._sentinel}'\n".encode())
        await self._process.stdin.drain()

        # read output from the process, until the sentinel is found
        try:
            async with asyncio.timeout(self._timeout):
                while True:
                    await asyncio.sleep(self._output_delay)
                    output = self._process.stdout._buffer.decode()
                    error = self._process.stderr._buffer.decode()
                    if self._sentinel in output:
                        output = output[: output.index(self._sentinel)]
                        break
        except TimeoutError:
            self._timed_out = True
            stdout_truncated = output[:10000] + "<response clipped>" if len(output) > 10000 else output
            stderr_truncated = error[:10000] + "<response clipped>" if len(error) > 10000 else error
            
            stdout_file = None
            stderr_file = None
            
            try:
                with tempfile.NamedTemporaryFile(mode='w', prefix='bash_stdout_', suffix='.log', delete=False) as f:
                    f.write(output)
                    stdout_file = f.name
                
                with tempfile.NamedTemporaryFile(mode='w', prefix='bash_stderr_', suffix='.log', delete=False) as f:
                    f.write(error)
                    stderr_file = f.name
                
                raise ToolError(
                    f"timed out: bash has not returned in {self._timeout} seconds and must be restarted.\n"
                    f"Full logs saved to:\n"
                    f"  STDOUT: {stdout_file}\n"
                    f"  STDERR: {stderr_file}\n"
                    f"Truncated output:\n"
                    f"  STDOUT: {stdout_truncated}\n"
                    f"  STDERR: {stderr_truncated}",
                ) from None
            except Exception:
                raise ToolError(
                    f"timed out: bash has not returned in {self._timeout} seconds and must be restarted. "
                    f"STDOUT: {stdout_truncated}\n STDERR: {stderr_truncated}",
                ) from None

        if output.endswith("\n"):
            output = output[:-1]

        if error.endswith("\n"):
            error = error[:-1]

        self._process.stdout._buffer.clear()
        self._process.stderr._buffer.clear()

        return CLIResult(output=output, error=error)


class BashTool:
    """
    A tool that allows the agent to run bash commands.
    
    Anti-cheat measures:
    - Git history commands (log, show, reflog) are blocked
    - Access to /evaluation/ directory is blocked
    - Agent runs as non-root user (uid 1000)
    
    Allowed git commands:
    - git diff, git status, git add, git commit (for tracking own changes)
    """

    _session: _BashSession | None

    def __init__(self):
        self._session = None

    async def __call__(self, command: str | None = None, restart: bool = False, **kwargs) -> ToolResult:
        if restart:
            if self._session:
                self._session.stop()
            self._session = _BashSession()
            await self._session.start()

            return ToolResult(system="tool has been restarted.")

        if self._session is None:
            self._session = _BashSession()
            await self._session.start()

        if command is not None:
            return await self._session.run(command)

        raise ToolError("no command provided.")