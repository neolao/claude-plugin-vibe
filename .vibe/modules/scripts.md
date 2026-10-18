# Module: scripts

**Role:** Shell utilities shipped with the plugin. `scripts/` holds the status-line script; the two skill scripts (`skills/tasks/scripts/tasks.sh`, `skills/usage-report/scripts/usage-report.sh`, POSIX sh + awk, tested by `evals/tasks-script-test.sh` and `evals/usage-report-script-test.sh`) are described with their skills in `modules/skills.md`.
**Files:** `scripts/subagent-statusline.sh`
**Exports:** reads a JSON payload (`{columns, tasks: [{id, name, status, description, tokenCount, ...}]}`) on stdin via `jq`, emits one `{id, content}` JSON line per task row (status icon + bold name + description + token count, truncated to `columns`); on invalid input, logs a diagnostic to stderr and exits cleanly instead of failing silently.
