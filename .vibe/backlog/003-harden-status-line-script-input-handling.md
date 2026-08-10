---
status: todo
---
# Harden Status Line Script Input Handling

## Description
`scripts/subagent-statusline.sh` reads its whole input with no size limit, and exits with code `0` even when `jq` fails to parse it (only a stderr line marks the failure). This is fine for today's known caller, but leaves no way to detect a bad payload from the exit code alone.

## Acceptance Criteria
- [ ] The script rejects (or safely truncates) an input above a defined size, with a clear stderr message.
- [ ] A documented way exists to tell a parse failure apart from a normal empty render (exit code, sentinel output, or similar) without breaking the status line UI on failure.
- [ ] `.vibe/modules/scripts.md` reflects the new behavior after the change.

## Notes
Raised by `/vibe:review` (review-robustness, Low). The current "always exit 0" choice is intentional (avoid breaking the UI) — keep that property while making failures detectable.
