# Module: scripts

**Role:** Shell utilities shipped with the plugin. Currently one script: renders the custom subagent status-line panel shown while review or feature/fix agents run in parallel.
**Files:** `scripts/subagent-statusline.sh`
**Exports:** reads a JSON payload (`{columns, tasks: [{id, name, status, description, tokenCount, ...}]}`) on stdin via `jq`, emits one `{id, content}` JSON line per task row (status icon + bold name + description + token count, truncated to `columns`); on invalid input, logs a diagnostic to stderr and exits cleanly instead of failing silently.
