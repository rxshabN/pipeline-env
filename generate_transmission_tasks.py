import json
import os

with open("hud_tasks.json", "r") as f:
    tasks = json.load(f)

output_code = """from hud_controller.spec import EnvironmentState, Grade, problem
from hud_controller.graders import AgentPatchGrader

# AUTOMATICALLY GENERATED FROM hud_tasks.json
"""

for task in tasks:
    func_name = task['task_id'].replace("-", "_")
    safe_msg = task['message'].replace('"', "'")
    
    task_code = f"""
@problem(
    id="{task['task_id']}",
    description=\"\"\"
    {safe_msg}
    
    Fix the issue in Transmission. 
    The environment is reset to the commit BEFORE this fix.
    \"\"\",
    hints=[],
    difficulty="hard",
    task_type="coding",
    review_level="no-review",
    base="{task['buggy_commit']}",
    test="{task['golden_commit']}", 
    golden="{task['golden_commit']}",
)
def {func_name}(state: EnvironmentState) -> Grade:
    return Grade.from_subscores([
        AgentPatchGrader.grade(
            state=state,
            weight=1.0,
            base="{task['buggy_commit']}",
            test="{task['golden_commit']}", 
            golden="{task['golden_commit']}",
            jest_test_files={json.dumps(task['files'])}, 
        )
    ])
"""
    output_code += task_code

output_path = "src/hud_controller/extractors/transmission_tasks.py"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w") as f:
    f.write(output_code)

print(f"✅ Generated {len(tasks)} tasks in {output_path}")