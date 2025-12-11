import asyncio
import logging
import os
import subprocess
import shutil
from pathlib import Path
from typing import Any

try:
    from .manual_dinit import ServiceLoader, SimpleDinit
except ImportError:
    ServiceLoader = None
    SimpleDinit = None

logger = logging.getLogger(__name__)

def subprocess_run(cmd, cwd=None, check=True, shell=False):
    """Helper to run shell commands with logging."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd, check=check, capture_output=True, text=True, shell=shell
        )
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {cmd}\nStderr: {e.stderr}\nStdout: {e.stdout}")
        raise e

async def start_dinit():
    """
    Starts background services (GUI, etc) if configured.
    """
    dinit_dir = Path("/etc/dinit.d")
    
    if not dinit_dir.exists():
        logger.info("/etc/dinit.d not found. Skipping service startup.")
        return

    if ServiceLoader is None:
        logger.warning("manual_dinit module not found. Skipping services.")
        return

    logger.info("Starting dinit services...")
    loader = ServiceLoader(dinit_dir)
    services = loader.load_all()
    if services:
        engine = SimpleDinit(services)
        engine.start("boot")
    else:
        logger.info("No services found to start.")

def setup_codebase(base: str, test: str, golden: str):
    repo_path = os.environ.get("REPO_PATH", "/home/ubuntu/repo")
    secure_git = os.environ.get("SECURE_GIT_DIR", "/evaluation/secure_git/repo.git")
    
    logger.info("=" * 50)
    logger.info(f"SETTING UP GO TASK")
    logger.info(f"   Buggy commit: {base[:8]}")
    logger.info(f"   Golden commit: {golden[:8] if golden else 'N/A'}")
    logger.info("=" * 50)
    
    try:
        logger.info("Cleaning workspace...")
        if os.path.exists(repo_path):
            subprocess_run(f"rm -rf {repo_path}/*", shell=True)
            subprocess_run(f"rm -rf {repo_path}/.* 2>/dev/null || true", shell=True)
        else:
            os.makedirs(repo_path, exist_ok=True)

        logger.info(f"Extracting source at buggy commit {base[:8]}...")
        
        archive_cmd = f"git --git-dir={secure_git} archive {base} | tar -x -C {repo_path}"
        subprocess_run(archive_cmd, shell=True)
        
        if golden:
            logger.info(f"💉 Injecting tests from golden commit {golden[:8]}...")
            test_archive_cmd = (
                f"git --git-dir={secure_git} archive {golden} -- test/ 2>/dev/null | "
                f"tar -x -C {repo_path} 2>/dev/null || true"
            )
            subprocess_run(test_archive_cmd, shell=True)
        
        logger.info("Initializing clean git repo for agent...")
        
        for item in Path(repo_path).rglob('.git'):
            if item.is_dir():
                shutil.rmtree(item)
            elif item.is_file():
                item.unlink()
        
        subprocess_run(["git", "init"], cwd=repo_path)
        subprocess_run(["git", "add", "."], cwd=repo_path)
        subprocess_run(
            ["git", "commit", "-m", "Initial state (contains bug to fix)"],
            cwd=repo_path
        )
        
        subprocess_run(["chown", "-R", "ubuntu:ubuntu", repo_path])
        
        logger.info("=" * 50)
        logger.info("SETUP COMPLETE")
        logger.info("=" * 50)
        logger.info(f"   Workspace: {repo_path}")
        logger.info("   ")
        logger.info("   Agent instructions:")
        logger.info("   • Read tests in *_test.go files to understand expected behavior")
        logger.info("   • Modify source files to fix the bug")
        logger.info("   • Call evaluate() when done")
        logger.info("   • DO NOT run go test manually (use evaluate)")
        
    except Exception as e:
        logger.error(f"Setup failed: {e}")
        raise

async def default_setup(template: dict[str, Any]) -> None:
    """Default setup function that initializes the environment for coding tasks."""
    logger.info("=== ENVIRONMENT SETUP ===")
    logger.info(f"Task: {template.get('id', 'unknown')}")

    await start_dinit()

    await asyncio.to_thread(
        setup_codebase,
        base=template["base"],
        test=template["test"],
        golden=template["golden"],
    )
    
    logger.info("Environment ready for agent.")