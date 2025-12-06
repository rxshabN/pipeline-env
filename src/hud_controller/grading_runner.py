#!/usr/bin/env python3

import logging
import os
import subprocess
import sys
import threading
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path
from .utils import merge_junits

logger = logging.getLogger(__name__)

class GradingRunner:
    """Handles the grading workflow for C++/Transmission."""

    def __init__(
        self,
        base: str,
        test: str,
        golden: str,
        playwright_test_files: list[str] | None = None,
        mocha_test_files: list[str] | None = None,
        test_files: list[str] | None = None,
        test_patch_path: str = "/home/ubuntu/test.patch",
        golden_patch_path: str = "/home/ubuntu/golden.patch",
        only_server: bool = False,
    ):
        self.use_base = base
        self.use_test = test
        self.use_golden = golden
        self.test_patch_path = test_patch_path
        self.golden_patch_path = golden_patch_path
        self.test_files = test_files or []
        self.grade_working_dir = "/tmp/grading_workspace_" + str(uuid.uuid4())
        
        self.original_repo_path = os.environ.get("REPO_PATH", "/home/ubuntu/repo")

    def _format_junit_xml(self, test_name: str, message: str, stdout: str, stderr: str) -> str:
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
  <testsuite name="{test_name}" tests="1" failures="1" errors="0" skipped="0">
    <testcase classname="{test_name}" name="test{test_name}" time="0.0">
      <failure type="TestFailure">\n{message}\n</failure>
      <system-out>\n{stdout}\n</system-out>
      <system-err>\n{stderr}\n</system-err>
    </testcase>
  </testsuite>
</testsuites>"""

    def _calculate_score(self, junit_xml_content: str) -> float:
        """
        Parses JUnit XML to calculate a dense reward score.
        Score distribution:
        - 0.0: Build failure (handled before this function)
        - 0.1: Build success, but all tests failed.
        - 0.1 -> 1.0: Linearly scaled based on passing tests.
        """
        try:
            root = ET.fromstring(junit_xml_content)
            total_tests = 0
            failures = 0
            errors = 0
            
            suites = root.findall('testsuite') if root.tag == 'testsuites' else [root]
            
            for suite in suites:
                tests_attr = suite.get('tests')
                if tests_attr:
                    total_tests += int(tests_attr)
                    failures += int(suite.get('failures', 0))
                    errors += int(suite.get('errors', 0))
                else:
                    total_tests += len(suite.findall('testcase'))
                    failures += len(suite.findall("testcase/failure"))
                    errors += len(suite.findall("testcase/error"))

            if total_tests == 0:
                return 0.1

            passed = total_tests - (failures + errors)
            
            ratio = passed / total_tests
            final_score = 0.1 + (0.9 * ratio)
            
            return round(final_score, 4)

        except ET.ParseError:
            logger.error("Failed to parse JUnit XML for scoring")
            return 0.0

    def run_tests(self) -> str:
        """Run CTest and return JUnit XML output."""
        logger.info(f"Running CTest in {self.grade_working_dir}")
        
        build_dir = Path(self.grade_working_dir) / "build"
        
        cmd = [
            "ctest",
            "--output-junit", "junit_results.xml",
            "--output-on-failure",
            "-j", str(os.cpu_count() or 2)
        ]

        result = subprocess.run(
            cmd,
            cwd=build_dir,
            capture_output=True,
            text=True,
        )
        
        logger.info(f"Tests completed with code: {result.returncode}")
        
        xml_path = build_dir / "junit_results.xml"
        if xml_path.exists():
            with open(xml_path) as f:
                return f.read()
        else:
            return self._format_junit_xml("CTestCrash", "CTest failed to generate XML", result.stdout, result.stderr)

    def run_grading(self) -> tuple[float, dict]:
        """Run the complete C++ grading workflow."""
        logger.info("Starting grading workflow")

        logger.info(f"Copying repo to {self.grade_working_dir}")
        subprocess.run(["cp", "-r", self.original_repo_path, self.grade_working_dir], check=True)

        if self.test_files and self.use_golden:
            files_to_reset = [f for f in self.test_files if f.startswith("tests/") or "test" in f.lower()]
            
            if files_to_reset:
                logger.info(f"🛡️ Anti-Cheat: Resetting {len(files_to_reset)} test files to golden state...")
                try:
                    subprocess.run(
                        ["git", "checkout", self.use_golden, "--"] + files_to_reset,
                        cwd=self.grade_working_dir,
                        check=True,
                        capture_output=True
                    )
                except subprocess.CalledProcessError as e:
                    logger.error(f"Failed to reset tests: {e.stderr}")
                    return 0.0, {"error": "Anti-Cheat test reset failed", "details": e.stderr}

        if os.path.exists(self.test_patch_path):
            logger.info("Applying test patch")
            with open(self.test_patch_path) as f:
                subprocess.run(["git", "apply"], check=True, cwd=self.grade_working_dir, input=f.read().encode("utf-8"))

        logger.info(f"Compiling in {self.grade_working_dir}")
        
        build_process = subprocess.run(
            ["ninja"],
            cwd=str(Path(self.grade_working_dir) / "build"),
            capture_output=True,
            text=True
        )
        
        if build_process.returncode != 0:
            logger.info(f"Compilation failed: {build_process.stderr}")
            xml_content = self._format_junit_xml("CompileError", "Build Failed", build_process.stdout, build_process.stderr)
            return 0.0, {"junit": xml_content}

        logger.info("Compilation successful.")

        junit_xml = self.run_tests()
        
        score = self._calculate_score(junit_xml)
        logger.info(f"Calculated Score: {score}")

        return score, {"junit": junit_xml}