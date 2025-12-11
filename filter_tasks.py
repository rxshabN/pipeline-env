import argparse
import json
import os
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

def run_single_task(task_id, run_index):
    """
    Executes a single task using the OFFICIAL HUD CLI.
    """
    start_time = time.time()
    try:
        # We call 'hud eval' (the library), NOT 'hud_eval' (your local script)
        # This allows HUD to handle the cloud connection defined in the JSON.
        result = subprocess.run(
            [
                "hud", "eval", "pipeline_benchmark.json",  # Updated filename
                "--task-ids", task_id,
                "--agent", "claude",  # Explicitly set agent to avoid interactive prompt
                "--yes",              # Skip confirmation prompts
                "--verbose"           # Ensure logs are printed so we can capture the score
            ],
            capture_output=True,
            text=True,
            check=False,
            # We need shell=True on Windows sometimes for PATH resolution, 
            # but usually False is safer. If 'hud' isn't found, try shell=True.
            shell=(os.name == 'nt') 
        )
        duration = time.time() - start_time
        
        # 1. Check Infrastructure Health
        # If hud eval returns non-zero, it likely crashed.
        if result.returncode != 0:
            # Check for specific "Connection closed" errors which are infra failures
            if "Connection closed" in result.stderr:
                return task_id, False, False, duration
            # Otherwise it might just be a task failure, but let's be conservative
            return task_id, False, False, duration

        # 2. Check Test Results
        # We parse the logs for the specific score log from your grading_runner.py
        score = 0.0
        # Combine stdout and stderr because different tools log to different pipes
        logs = result.stderr + "\n" + result.stdout
        
        if "Calculated Score:" in logs:
            for line in logs.splitlines():
                if "Calculated Score:" in line:
                    try:
                        # Format is usually "INFO: ... Calculated Score: 1.0"
                        score_str = line.split("Calculated Score:")[-1].strip()
                        score = float(score_str)
                    except ValueError:
                        pass
        
        # We also check for the new log format from grading_runner.py
        if "Score:" in logs:
             for line in logs.splitlines():
                if "Score:" in line and "INFO" in line: # e.g. INFO: ... Score: 0.1000
                     try:
                        score_str = line.split("Score:")[-1].strip()
                        score = float(score_str)
                     except ValueError:
                        pass


        # If Score > 0, the agent passed the test. 
        # For a benchmark of BUGS, we want the agent to FAIL (initially), 
        # but here we are validating the TASK.
        # Wait - if we are running the *buggy* commit, the tests SHOULD fail (Score 0).
        # But your setup runs the *Agent* to fix it. 
        # So we want the Agent to SUCCEED (Score 1.0) to prove the task is solvable?
        # NO. You said: "find issues where the AI fails consistently".
        # So we want Score == 0.0 (Agent failed to fix it).
        
        agent_succeeded = score > 0.0
        
        return task_id, True, agent_succeeded, duration

    except Exception as e:
        print(f"Error running {task_id}: {e}")
        return task_id, False, False, 0

def main():
    parser = argparse.ArgumentParser(description="Filter tasks for RL training.")
    parser.add_argument("--repeats", type=int, default=10, help="Times to run each task")
    parser.add_argument("--concurrency", type=int, default=20, help="Concurrent cloud jobs")
    parser.add_argument("--input", default="hud_tasks.json", help="Source raw tasks file")
    args = parser.parse_args()

    import os
    if not os.path.exists("pipeline_benchmark.json"):
        print("❌ Error: pipeline_benchmark.json not found. Run generate_benchmark.py first.")
        sys.exit(1)

    # 1. Load Data
    with open(args.input, "r") as f:
        raw_tasks = json.load(f)
    
    # Only verify tasks that are actually in the benchmark config
    with open("pipeline_benchmark.json", "r") as f:
        bench_tasks = json.load(f)
        valid_ids = set(t["id"] for t in bench_tasks)
        
    tasks_to_run = [t for t in raw_tasks if t["task_id"] in valid_ids]

    print(f"🚀 Starting Curation for {len(tasks_to_run)} tasks.")
    print(f"   Config: {args.repeats} repeats, {args.concurrency} concurrent.")
    print("   Goal: Find 'Hard' tasks where Agent consistently FAILS (Score 0).")

    # 2. Execute
    task_results = defaultdict(list)
    
    # We use ThreadPoolExecutor because 'subprocess' releases the GIL, 
    # allowing effective concurrency for IO-bound CLI calls.
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = []
        for task in tasks_to_run:
            t_id = task["task_id"]
            for i in range(args.repeats):
                futures.append(executor.submit(run_single_task, t_id, i))

        completed = 0
        total = len(futures)
        for future in as_completed(futures):
            t_id, infra_ok, agent_success, dur = future.result()
            task_results[t_id].append((infra_ok, agent_success))
            completed += 1
            
            # Progress bar style output
            status_char = "✅" if agent_success else "❌" # Green if agent fixed it, Red if failed
            if not infra_ok: status_char = "💥"
            
            print(f"[{completed}/{total}] {status_char} {t_id} ({dur:.1f}s)")

    # 3. Filter and Save
    kept_tasks = []
    print("\n=== Filtering Results ===")
    
    for task in tasks_to_run:
        t_id = task["task_id"]
        runs = task_results[t_id]
        
        infra_failures = sum(1 for r in runs if not r[0])
        agent_successes = sum(1 for r in runs if r[1])
        total_runs = len(runs)
        
        if total_runs == 0: continue

        # Criteria 1: Infrastructure must be stable (0 crashes)
        if infra_failures > 0:
            print(f"DROP {t_id}: Infra unstable ({infra_failures}/{total_runs} crashed)")
            continue
            
        # Criteria 2: Agent must FAIL consistently (Hard task)
        # If agent fixed it even once (success > 0), it might be too easy or flaky.
        if agent_successes > 0:
            print(f"DROP {t_id}: Too easy/Flaky ({agent_successes}/{total_runs} agent successes)")
            continue
            
        # Criteria 3: Agent passed 0 times -> Perfect candidate for RL training
        print(f"KEEP {t_id}: Stable Failure (Agent 0/{total_runs})")
        kept_tasks.append(task)

    output_file = "hud_tasks_final.json"
    with open(output_file, "w") as f:
        json.dump(kept_tasks, f, indent=2)

    print(f"\n✅ Saved {len(kept_tasks)} filtered tasks to {output_file}")

if __name__ == "__main__":
    main()