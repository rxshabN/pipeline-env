import json
import os

with open("hud_tasks.json", "r") as f:
    raw_tasks = json.load(f)

benchmark_tasks = []

for t in raw_tasks:
    task = {
        "id": t["task_id"],
        
        "prompt": f"""You are working on task: {t['task_id']}

        DESCRIPTION:
        Fix the issue described: {t['message']}

        The environment is reset to the parent commit. Run tests to verify failure, then fix it.
        """,
        
        "mcp_config": {
            "local": {
                "command": "docker",
                "args": [
                    "run", 
                    "--rm", 
                    "-i",
                    "--network", "none",
                    "-v", f"{os.getcwd()}/src/hud_controller/extractors:/evaluation/src/hud_controller/extractors",
                    "hud-transmission-env"
                ]
            }
        },
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

with open("transmission_benchmark.json", "w") as f:
    json.dump(benchmark_tasks, f, indent=2)

print(f"Generated transmission_benchmark.json with {len(benchmark_tasks)} tasks.")