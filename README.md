# claude-plugin-vibe

A Claude Code plugin for **vibe coding**: the human stays Product Owner only — describing requirements and evaluating outcomes — while Claude writes, tests, reviews, and ships the code. All quality assurance is automated (TDD, lint, multi-agent review); nothing is meant to be tested manually.

## Skills (commands)

| Command | Purpose |
|---|---|
| `/vibe:init` | Initialize or regenerate the project's `CLAUDE.md` for vibe coding |
| `/vibe:backlog` | List or add feature backlog items (`.vibe/backlog/`) |
| `/vibe:feature` | Implement a new feature using TDD, then update the changelog |
| `/vibe:fix` | Fix a bug using TDD (reproduce first), then update the changelog |
| `/vibe:review` | Run a multi-agent code quality review and auto-apply fixes |
| `/vibe:sync` | Generate/update `.vibe/` — the codebase context map |
| `/vibe:changelog` | Update `CHANGELOG.md` from git history |
| `/vibe:docs` | Generate/refresh README managed sections and `docs/` |
| `/vibe:release` | Bump version, finalize the changelog, commit and tag a release |

## Review agents

`/vibe:review` orchestrates these specialized agents/skills in parallel:

- **Agents**: `review-architecture`, `review-complexity`, `review-ddd`, `review-dependencies`, `review-hygiene`, `review-naming`, `review-performance`, `review-robustness`, `review-security`, `review-solid`
- **Skills**: `review-tests`, `review-web-security`

Each focuses on one dimension only (see `/vibe:init`'s "Review agents" table for activation rules per project).

## Subagent status line

The plugin ships a `subagentStatusLine` (`settings.json` + `scripts/subagent-statusline.sh`), applied automatically once the plugin is enabled. It replaces the default `name · description · token count` row in the agent panel with a compact, color-coded line (status icon, bold name, description, token count) — most visible during `/vibe:review`, which runs up to 12 review agents/skills in parallel.

## Typical flow

1. `/vibe:init` once, to set up `CLAUDE.md` and `.vibe/`
2. `/vibe:backlog "some feature idea"` to queue work
3. `/vibe:feature 001` (or `/vibe:fix "bug description"`) to implement, TDD-first
4. `/vibe:review` periodically to catch quality issues
5. `/vibe:release patch|minor|major` to ship a version
