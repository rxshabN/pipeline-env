#!/usr/bin/env python3

import logging
import os
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
import time

logger = logging.getLogger(__name__)

class GradingRunner:
    """Handles the grading workflow for Tekton (Go) tasks."""

    def __init__(
        self,
        base: str,
        test: str,
        golden: str,
        test_files: list[str] | None = None,
        test_patch_path: str = "/home/ubuntu/test.patch",
        golden_patch_path: str = "/home/ubuntu/golden.patch",
        only_server: bool = False,
        playwright_test_files: list[str] | None = None,
        mocha_test_files: list[str] | None = None,
    ):
        self.use_base = base
        self.use_test = test
        self.use_golden = golden
        self.test_patch_path = test_patch_path
        self.golden_patch_path = golden_patch_path
        self.test_files = test_files or []
        
        self.repo_path = os.environ.get("REPO_PATH", "/home/ubuntu/repo")
        self.build_dir = Path(self.repo_path) 
        self.secure_git = os.environ.get("SECURE_GIT_DIR", "/evaluation/secure_git/repo.git")

    def _format_junit_xml(self, test_name: str, message: str, stdout: str, stderr: str) -> str:
        """Generate JUnit XML for error cases."""
        def escape(s):
            return (s.replace("&", "&amp;")
                      .replace("<", "&lt;")
                      .replace(">", "&gt;")
                      .replace('"', "&quot;"))
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
  <testsuite name="{escape(test_name)}" tests="1" failures="1" errors="0" skipped="0">
    <testcase classname="{escape(test_name)}" name="test" time="0.0">
      <failure type="TestFailure">{escape(message)}</failure>
      <system-out>{escape(stdout[:5000])}</system-out>
      <system-err>{escape(stderr[:5000])}</system-err>
    </testcase>
  </testsuite>
</testsuites>"""

    def _reset_test_files(self):
        if not self.use_golden: return
        logger.info("Anti-cheat: Resetting test files...")
        try:
            cmd = f"git --git-dir={self.secure_git} archive {self.use_golden} -- test/ | tar -x -C {self.repo_path}"
            subprocess.run(cmd, shell=True, check=True, capture_output=True)
            logger.info("Test files reset successfully")
        except subprocess.CalledProcessError:
            pass

    def _get_target_packages(self) -> list[str]:
        if not self.test_files: return ["./..."]
        packages = set()
        for filepath in self.test_files:
            if filepath.endswith('.go'):
                directory = os.path.dirname(filepath)
                if directory: packages.add(f"./{directory}")
                else: packages.add(".")
        
        if os.path.exists(os.path.join(self.repo_path, "test")):
             packages.add("./test/...")

        return sorted(list(packages))

    def _run_tests(self) -> tuple[str, float, float]:
        start_time = time.time()
        
        target_packages = self._get_target_packages()
        logger.info(f"Targeted Testing: {len(target_packages)} packages")
        
        merged_xml_parts = []
        
        total_packages = len(target_packages)
        passed_packages = 0

        PACKAGE_TIMEOUT_SECONDS = 150 

        for pkg in target_packages:
            logger.info(f"Testing package: {pkg}")
            pkg_start = time.time()
            
            safe_pkg_name = pkg.replace('/', '_').replace('.', '').strip('_')
            if not safe_pkg_name: safe_pkg_name = "root"
            pkg_xml_file = f"junit_{safe_pkg_name}.xml"
            
            cmd = [
                "gotestsum",
                "--junitfile", pkg_xml_file,
                "--format", "standard-verbose",
                "--",
                "-mod=vendor", 
                "-short",
                "-v",
                pkg
            ]
            
            try:
                result = subprocess.run(
                    cmd,
                    cwd=str(self.repo_path),
                    capture_output=True,
                    text=True,
                    timeout=PACKAGE_TIMEOUT_SECONDS
                )
                
                if result.returncode == 0:
                    logger.info(f"Package {pkg} PASSED")
                    passed_packages += 1
                else:
                    logger.warning(f"Package {pkg} FAILED (exit {result.returncode})")
                
                xml_path = Path(self.repo_path) / pkg_xml_file
                if xml_path.exists():
                    with open(xml_path) as f:
                        content = f.read().replace('<?xml version="1.0" encoding="UTF-8"?>', '')
                        merged_xml_parts.append(content)
                
            except subprocess.TimeoutExpired:
                logger.error(f"Package {pkg} TIMED OUT (>{PACKAGE_TIMEOUT_SECONDS}s)")
                merged_xml_parts.append(f'<testsuite name="{pkg}" tests="1" failures="1"><testcase name="Timeout"><failure message="Timeout">Test package timed out</failure></testcase></testsuite>')
                continue

        duration = time.time() - start_time

        final_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<testsuites>\n' + "\n".join(merged_xml_parts) + "\n</testsuites>"
        
        package_score = 0.0
        if total_packages > 0:
            package_score = float(passed_packages) / float(total_packages)
            
        logger.info(f"Partial Score: {passed_packages}/{total_packages} packages passed = {package_score:.2f}")

        return final_xml, duration, package_score

    def run_grading(self) -> tuple[float, dict]:
        """Run the complete grading workflow."""
        total_start = time.time()
        logger.info("=" * 60)
        logger.info("GRADING STARTED")
        logger.info("=" * 60)

        try:
            self._reset_test_files()

            if os.path.exists(self.test_patch_path):
                subprocess.run(["git", "apply", "--allow-empty"], cwd=self.repo_path, input=open(self.test_patch_path, 'rb').read(), check=False)

            junit_xml, test_duration, score = self._run_tests()
                        
            total_duration = time.time() - total_start
            
            logger.info("=" * 60)
            logger.info(f"GRADING COMPLETE")
            logger.info(f"   Score: {score:.4f}")
            logger.info("=" * 60)

            return score, {
                "junit": junit_xml,
                "test_duration": test_duration,
                "total_duration": total_duration
            }
            
        except Exception as e:
            total_duration = time.time() - total_start
            logger.exception(f"Grading failed: {e}")
            return 0.0, {"error": str(e)}