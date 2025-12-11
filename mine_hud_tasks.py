import git
import json
import os
import logging
from collections import Counter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

REPO_PATH = "env/pipeline"

def is_test_file(filepath: str) -> bool:
    filepath_lower = filepath.lower()

    if filepath_lower.endswith('_test.go'):
        return True
        
    if 'test/' in filepath_lower or 'tests/' in filepath_lower:
        return True

    return False

def is_source_code_file(filepath: str) -> bool:
    return filepath.endswith('.go')

def has_non_test_code_changes(files: list) -> bool:
    for f in files:
        if is_source_code_file(f) and not is_test_file(f):
            return True
    return False

def mine_tasks():    
    if not os.path.exists(REPO_PATH):
        logger.error(f"Repository not found at {REPO_PATH}. Did you initialize the submodule?")
        return

    try:
        repo = git.Repo(REPO_PATH)
        logger.info(f"Successfully opened repository at {REPO_PATH}")
    except Exception as e:
        logger.error(f"Could not open repo at {REPO_PATH}. Error: {e}")
        return

    tasks = []
    
    EXCLUDED_PREFIXES = ["feat", "perf", "chore", "build", "ci", "docs", "style", "test", "release"]
    
    FIX_KEYWORDS = ["fix", "resolve", "close", "bug", "issue"]

    logger.info("Starting task mining from git history...")
    
    stats = Counter()
    commits_checked = 0
    
    MAX_COUNT = 20000
    
    try:
        for commit in repo.iter_commits('main', max_count=MAX_COUNT): 
            commits_checked += 1
            if commits_checked % 1000 == 0:
                logger.info(f"Scanned {commits_checked} commits... Found {len(tasks)} valid tasks so far.")

            summary = str(commit.summary).strip().lower()
            msg = str(commit.message).lower()
            
            if not commit.parents:
                continue

            if any(summary.startswith(p) for p in EXCLUDED_PREFIXES):
                stats['skipped_prefix'] += 1
                continue

            if not any(k in msg for k in FIX_KEYWORDS):
                stats['skipped_no_keyword'] += 1
                continue
                
            try:
                diffs = commit.parents[0].diff(commit)
                files = [d.b_path for d in diffs if d.b_path]
            except Exception as e:
                logger.warning(f"Could not get diff for commit {commit.hexsha}: {e}")
                continue
            
            has_code = any(f.endswith('.go') for f in files)
            if not has_code:
                stats['skipped_no_go_code'] += 1
                continue
            
            has_test = any(is_test_file(f) for f in files)
            if not has_test:
                stats['skipped_no_tests'] += 1
                continue
            
            if not has_non_test_code_changes(files):
                stats['skipped_only_tests_changed'] += 1
                continue
            
            if len(files) <= 15:
                stats['skipped_too_small'] += 1
                continue
            
            task_id = f"tekton-{commit.hexsha[:7]}"
            
            tasks.append({
                "task_id": task_id,
                "buggy_commit": commit.parents[0].hexsha,
                "golden_commit": commit.hexsha,
                "message": commit.summary.strip(),
                "files": files
            })
            stats['accepted'] += 1
            
    except Exception as e:
        logger.error(f"Error during mining loop: {e}")

    logger.info("=" * 40)
    logger.info(f"Mining Complete.")
    logger.info(f"Commits scanned: {commits_checked}")
    logger.info(f"Valid tasks found: {len(tasks)}")
    logger.info("Stats:")
    for key, value in stats.items():
        logger.info(f"  {key}: {value}")
    logger.info("=" * 40)
    
    output_file = "hud_tasks.json"
    with open(output_file, "w") as f:
        json.dump(tasks, f, indent=2)
    logger.info(f"Saved tasks to {output_file}")

if __name__ == "__main__":
    mine_tasks()