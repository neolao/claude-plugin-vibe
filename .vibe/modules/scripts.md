# Module: scripts

**Role:** Shell utilities shipped with the plugin. Currently one script: renders the custom subagent status-line panel shown during `/vibe:review` (up to 12 parallel agents).
**Files:** `scripts/subagent-statusline.sh`
**Exports:** reads a JSON payload (`{columns, tasks: [{id, name, status, description, tokenCount, ...}]}`) on stdin via `jq`, emits one `{id, content}` JSON line per task row (status icon + bold name + description + token count, truncated to `columns`).
**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) — wired in via the `subagentStatusLine` hook in `settings.json`
