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

    def _calculate_score(self, junit_xml_content: str) -> float:
        """
        Calculate score from JUnit XML test results.
        Returns 1.0 if ALL tests pass, 0.0 otherwise.
        """
        try:
            root = ET.fromstring(junit_xml_content)
            total_tests = 0
            failures = 0
            errors = 0
            skipped = 0
            
            suites = root.findall('testsuite') if root.tag == 'testsuites' else [root]
            
            for suite in suites:
                tests_attr = suite.get('tests')
                if tests_attr:
                    total_tests += int(tests_attr)
                    failures += int(suite.get('failures', 0))
                    errors += int(suite.get('errors', 0))
                    skipped += int(suite.get('skipped', 0))
                else:
                    total_tests += len(suite.findall('testcase'))
                    failures += len(suite.findall("testcase/failure"))
                    errors += len(suite.findall("testcase/error"))
                    skipped += len(suite.findall("testcase/skipped"))

            if failures > 0 or errors > 0:
                logger.info(f"Tests failed: {failures} failures, {errors} errors")
                return 0.0
            
            if total_tests == 0:
                logger.warning("No tests found in JUnit XML")
                return 0.0
                        
            logger.info(f"All {total_tests} tests passed")
            return 1.0

        except ET.ParseError as e:
            logger.error(f"Failed to parse JUnit XML: {e}")
            return 0.0

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

    def _run_tests(self) -> tuple[str, float]:
        start_time = time.time()
        
        target_packages = self._get_target_packages()
        logger.info(f"🎯 Targeted Testing: {len(target_packages)} packages")
        
        merged_xml_parts = []
        overall_success = True
        failure_reason = ""

        for pkg in target_packages:
            logger.info(f"⏳ Testing package: {pkg}")
            pkg_start = time.time()
            
            pkg_xml_file = f"junit_{pkg.replace('/', '_').replace('.', '')}.xml"
            
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
                    timeout=60
                )
                
                if result.returncode != 0:
                    logger.warning(f"Package {pkg} FAILED (exit {result.returncode})")
                    overall_success = False
                    failure_reason = f"Test failure in {pkg}\n{result.stdout[:500]}"
                
                xml_path = Path(self.repo_path) / pkg_xml_file
                if xml_path.exists():
                    with open(xml_path) as f:
                        content = f.read().replace('<?xml version="1.0" encoding="UTF-8"?>', '')
                        merged_xml_parts.append(content)
                
                logger.info(f"Package {pkg} completed in {time.time() - pkg_start:.1f}s")

            except subprocess.TimeoutExpired:
                overall_success = False
                merged_xml_parts.append(f'<testsuite name="{pkg}" tests="1" failures="1"><testcase name="Timeout"><failure message="Timeout">Test package timed out</failure></testcase></testsuite>')
                break

        duration = time.time() - start_time

        final_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<testsuites>\n' + "\n".join(merged_xml_parts) + "\n</testsuites>"
        
        if not overall_success and "Timeout" in failure_reason:
             return self._format_junit_xml("FatalError", failure_reason, "", ""), duration

        return final_xml, duration

    def run_grading(self) -> tuple[float, dict]:
        """Run the complete grading workflow."""
        total_start = time.time()
        logger.info("=" * 60)
        logger.info("🎯 GRADING STARTED")
        logger.info("=" * 60)

        try:
            self._reset_test_files()

            if os.path.exists(self.test_patch_path):
                subprocess.run(["git", "apply", "--allow-empty"], cwd=self.repo_path, input=open(self.test_patch_path, 'rb').read(), check=False)

            junit_xml, test_duration = self._run_tests()
            
            score = self._calculate_score(junit_xml)
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