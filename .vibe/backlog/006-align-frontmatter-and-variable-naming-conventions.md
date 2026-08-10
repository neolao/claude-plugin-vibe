---
status: todo
---
# Align Frontmatter And Variable Naming Conventions

## Description
A few names in the plugin's own data shapes and script don't follow their neighbors' convention: backlog frontmatter uses `depends_on` (snake_case) while skill frontmatter uses `argument-hint`/`user-invocable` (kebab-case); the status-line script abbreviates `$desc` while its siblings are spelled out in full; and the `current` field in `.vibe/auto-state.md` isn't self-descriptive out of context.

## Acceptance Criteria
- [ ] One convention is picked and documented for multi-word frontmatter keys plugin-wide (kebab-case or snake_case), and applied consistently — or the split is documented as intentional in `.vibe/models.md`.
- [ ] `$desc` in `scripts/subagent-statusline.sh` is renamed to `$description`, matching its sibling variables.
- [ ] The `current` field in `.vibe/auto-state.md` / `skills/auto/SKILL.md` is renamed to something self-descriptive (e.g. `current-item`).
- [ ] Every consumer of a renamed field is updated together, so nothing silently breaks.

## Notes
Raised by `/vibe:review` (review-naming, Low). Touches `.vibe/models.md`, `skills/auto/SKILL.md`, `skills/backlog/SKILL.md`, and the script.
