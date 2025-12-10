import argparse
import json
import os
from pathlib import Path

def create_rich_prompt(task):
    files = task.get("files", [])
    files_list = "\n".join([f"- {f}" for f in files]) if files else "See repository"
    
    return f"""## Task: {task['task_id']}

### Bug Description
{task['message']}

### Files to Modify
The following files need to be fixed:
{files_list}

### Your Task
1. Read and understand the bug description above
2. Examine the relevant source files in `/home/ubuntu/repo/`
3. Analyze the test files in `/home/ubuntu/repo/tests/` to understand expected behavior
4. Modify the source files to fix the bug

### 🛑 CRITICAL RULES - READ THESE CAREFULLY BEFORE BEGINNING 🛑

#### 1. NO BUILD OR TEST EXECUTION
* **DO NOT** run `ninja`, `make`, `cmake`, `configure`, or `ctest`.
* The environment is **Read-Only** for build artifacts. Attempts to build will crash the environment.
* Your code is built and tested **AUTOMATICALLY** by the evaluation system when you submit.

#### 2. NO HELPER SCRIPTS (Anti-Timeout Policy)
* **DO NOT** create or run Python/Shell scripts (e.g., `/tmp/convert.py`) to generate code, map variables, or analyze files.
* **Requirement:** You must edit the files **DIRECTLY** using `str_replace_editor` or `sed`. Do the work yourself; do not write code/scripts to do the work.

#### 3. NO MASSIVE OUTPUT
* **DO NOT** run commands that output hundreds of lines (e.g., `grep` without `head`, printing full arrays, or listing all files).
* **Requirement:** Always pipe commands to `head -n 20`. Verify logic on a small sample (1-2 files), then apply it broadly.

#### 4. SECURITY & SCOPE
* **ONLY** modify the source files listed above.
* **DO NOT** touch `CMakeLists.txt`, hidden `.git` directories, or build scripts.

### Repository Location
`/home/ubuntu/repo/`
"""

def main():
    parser = argparse.ArgumentParser(description="Generate the benchmark JSON file.")
    parser.add_argument("--image", type=str, help="The HUD Cloud Image ID (from `hud push`).")
    args = parser.parse_args()

    source_file = "hud_tasks.json" 
    
    if not os.path.exists(source_file):
        print(f"❌ Error: {source_file} not found.")
        return

    with open(source_file, "r") as f:
        raw_tasks = json.load(f)

    benchmark_tasks = []
    cwd = Path.cwd().as_posix()

    print(f"Generating benchmark from {source_file}...")

    for t in raw_tasks:
        prompt_text = create_rich_prompt(t)

        if args.image:
            mcp_config = {
                "default": {
                    "url": "https://mcp.hud.ai/v3/mcp",
                    "headers": {
                        "Authorization": "Bearer ${HUD_API_KEY}", 
                        "Mcp-Image": args.image
                    }
                }
            }
        else:
            mcp_config = {
                "local": {
                    "command": "docker",
                    "args": [
                        "run", 
                        "--rm", 
                        "-i", 
                        "--network", "none",
                        "-v", f"{cwd}/src/hud_controller/extractors:/evaluation/src/hud_controller/extractors",
                        "swe-bench-rl-env:0.1.0"
                    ]
                }
            }

        task = {
            "id": t["task_id"],
            "prompt": prompt_text,
            "mcp_config": mcp_config,
            "setup_tool": {
                "name": "setup_problem",
                "arguments": {"problem_id": t["task_id"]}
            },
            "evaluate_tool": {
                "name": "grade_problem",
                "arguments": {"problem_id": t["task_id"]}
            }
        }
        benchmark_tasks.append(task)

    output_file = "transmission_benchmark.json"
    with open(output_file, "w") as f:
        json.dump(benchmark_tasks, f, indent=2)

    print(f"Successfully generated {output_file}")
    if args.image:
        print(f"Configured for Cloud Image: {args.image}")
    else:
        print(f"Configured for Local Docker")

if __name__ == "__main__":
    main()