# import argparse
# import json
# import os
# from pathlib import Path

# def create_rich_prompt(task):
#     files = task.get("files", [])
#     files_list = "\n".join([f"- {f}" for f in files]) if files else "See repository"
    
#     return f"""## Task: {task['task_id']}

# ### Bug Description
# {task['message']}

# ### Files to Modify
# The following files need to be fixed:
# {files_list}

# ### Your Task
# 1. Read the bug description above.
# 2. Examine the source files in `/home/ubuntu/repo/`.
# 3. Analyze the test files in `/home/ubuntu/repo/test/` or files ending in `_test.go`.
#    **Note:** The tests are the "Source of Truth". They have already been updated to reflect the desired behavior. Use them as your specification.
# 4. Modify the source files to fix the bug.
# 5. Once you're confident with all your fixes, you can opt to create a summary of the changes made (do this once only).
# 6. Call the `evaluate_tool()` grader (`grade_problem`) to test your changes and evaluate your score.

# ### 🛑 CRITICAL RULES - READ CAREFULLY BEFORE BEGINNING 🛑

# #### 1. NO BUILD OR TEST EXECUTION
# * **DO NOT** run `go build`, `go test`, `make`, or `ko`.
# * The environment is **Read-Only** for build artifacts. Attempts to build will crash the environment.
# * Your code is built and tested **AUTOMATICALLY** by the evaluation system when you submit.

# #### 2. NO HELPER SCRIPTS
# * **DO NOT** create or run Python/Shell scripts (e.g., `/tmp/convert.py`) to generate code, map variables, or analyze files.
# * **Requirement:** You must edit the files **DIRECTLY** using `str_replace_editor` or `sed`. Do the work yourself; do not write code to do the work.

# #### 3. NO MASSIVE OUTPUT
# * **DO NOT** run commands that output hundreds of lines (e.g., `grep` without `head`, printing full arrays, or listing all files).
# * **Requirement:** Always pipe commands to `head -n 20`. Verify logic on a small sample (1-2 files), then apply it broadly.

# #### 4. SECURITY & SCOPE
# * **ONLY** modify the source files listed above.
# * **DO NOT** touch `go.mod`, `go.sum`, hidden `.git` directories, or build scripts.

# ### Repository Location
# `/home/ubuntu/repo/` (Tekton Pipeline)
# """

# def main():
#     parser = argparse.ArgumentParser(description="Generate the benchmark JSON file.")
#     parser.add_argument("--image", type=str, help="The HUD Cloud Image ID (from `hud push`).")
#     args = parser.parse_args()

#     source_file = "hud_tasks.json" 
    
#     if not os.path.exists(source_file):
#         print(f"❌ Error: {source_file} not found.")
#         return

#     with open(source_file, "r") as f:
#         raw_tasks = json.load(f)

#     benchmark_tasks = []
#     cwd = Path.cwd().as_posix()

#     print(f"Generating benchmark from {source_file}...")

#     for t in raw_tasks:
#         prompt_text = create_rich_prompt(t)

#         if args.image:
#             mcp_config = {
#                 "default": {
#                     "url": "https://mcp.hud.ai/v3/mcp",
#                     "headers": {
#                         "Authorization": "Bearer ${HUD_API_KEY}", 
#                         "Mcp-Image": args.image,
#                     }
#                 }
#             }
#         else:
#             mcp_config = {
#                 "local": {
#                     "command": "docker",
#                     "args": [
#                         "run", 
#                         "--rm", 
#                         "-i", 
#                         "--network", "none",
#                         "-v", f"{cwd}/src/hud_controller/extractors:/evaluation/src/hud_controller/extractors",
#                         "swe-bench-rl-env:0.1.0" 
#                     ]
#                 }
#             }

#         task = {
#             "id": t["task_id"],
#             "prompt": prompt_text,
#             "mcp_config": mcp_config,
#             "setup_tool": {
#                 "name": "setup_problem",
#                 "arguments": {"problem_id": t["task_id"]}
#             },
#             "evaluate_tool": {
#                 "name": "grade_problem",
#                 "arguments": {"problem_id": t["task_id"]}
#             }
#         }
#         benchmark_tasks.append(task)

#     output_file = "pipeline_benchmark.json"
#     with open(output_file, "w") as f:
#         json.dump(benchmark_tasks, f, indent=2)

#     print(f"Successfully generated {output_file}")
#     if args.image:
#         print(f"Configured for Cloud Image: {args.image}")
#     else:
#         print(f"Configured for Local Docker (swe-bench-rl-env:0.1.0)")

# if __name__ == "__main__":
#     main()

# without timeout:

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
1. Read the bug description above.
2. Examine the source files in `/home/ubuntu/repo/`.
3. Analyze the test files in `/home/ubuntu/repo/test/` or files ending in `_test.go`.
4. Modify the source files to fix the bug.
5. **VERIFY LOCALLY:** You are explicitly ALLOWED and ENCOURAGED to run `go test ./...` or `go test -v <package>` and `go build` in the terminal to verify your fix locally.
6. Once you're confident with all your fixes, you can opt to create a summary of the changes made (do this once only).
7. **SUBMIT:** Call the `evaluate()` grader (`grade_problem`) to test your changes and evaluate your score.

### 🛑 CRITICAL INSTRUCTIONS - READ CAREFULLY BEFORE BEGINNING 🛑

#### 1. ONE SHOT SUBMISSION
* **You can only call `evaluate()` ONCE at the end of your coding session.**
* This is your final submission.
* **Do not** use `grade_problem` to debug. Use local tools instead.

#### 2. USE LOCAL TOOLS
* Use the bash tool to run `go test` or `go build` as much as you need before submitting.
* Verify your logic on a small sample before applying broadly.

#### 3. SECURITY & SCOPE
* **ONLY** modify the source files listed above.
* **DO NOT** touch `go.mod`, `go.sum`, hidden `.git` directories, or build scripts.

### Repository Location
`/home/ubuntu/repo/` (Tekton Pipeline)
"""

def main():
    parser = argparse.ArgumentParser(description="Generate the benchmark JSON file.")
    parser.add_argument("--image", type=str, help="The HUD Cloud Image ID (from `hud push`).")
    args = parser.parse_args()

    source_file = "hud_final_tasks.json" 
    
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
                        "Mcp-Image": args.image,
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

    output_file = "pipeline_benchmark.json"
    with open(output_file, "w") as f:
        json.dump(benchmark_tasks, f, indent=2)

    print(f"Successfully generated {output_file}")
    if args.image:
        print(f"Configured for Cloud Image: {args.image}")
    else:
        print(f"Configured for Local Docker (swe-bench-rl-env:0.1.0)")

if __name__ == "__main__":
    main()