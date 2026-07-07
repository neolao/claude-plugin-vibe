# Module: plugin-manifest

**Role:** Declares the plugin's identity for Claude Code's plugin system and marketplace, and wires the status-line hook.
**Files:** `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `settings.json`
**Exports:**
- `plugin.json` — plugin metadata: `name: "vibe"`, `version`, `description`, `author`, `license`, `keywords`
- `marketplace.json` — marketplace listing: `name`, `description`, `owner`, `plugins[]` (each with `name`, `source`, `description`)
- `settings.json` — `subagentStatusLine` hook pointing at `scripts/subagent-statusline.sh`

**Depends on:** [`modules/scripts.md`](scripts.md)
