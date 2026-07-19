# Module: skills

**Role:** Slash-command definitions (`/vibe:*`) that drive the vibe-coding workflow — each is a self-contained instruction set read by Claude Code when the command is invoked.
**Files:** `skills/*/SKILL.md` (one directory per skill)
**Exports:**
- `/vibe:init` (`skills/init/SKILL.md`) — initialize/regenerate `CLAUDE.md` for vibe coding
- `/vibe:backlog` (`skills/backlog/SKILL.md`) — list, add, or remove (`remove NNN`, confirmation required, done items excluded) feature backlog items, committing each creation/removal itself
- `/vibe:feature` (`skills/feature/SKILL.md`) — implement a new feature via TDD (free-form description or backlog reference `NNN`), verify it for real via the native `verify` skill (assume-it's-broken posture), update CHANGELOG
- `/vibe:fix` (`skills/fix/SKILL.md`) — fix a bug via TDD (reproduce first; free-form description or backlog reference `NNN`), verify it for real via the native `verify` skill (assume-it's-broken posture), update CHANGELOG
- `/vibe:review` (`skills/review/SKILL.md`) — orchestrate multi-agent code quality review, re-checking the CLAUDE.md agent activation table against the current project state at each run (deliberate opt-outs respected), recording each run in `.vibe/last-review.md`
- `/vibe:sync` (`skills/sync/SKILL.md`) — generate/update `.vibe/` codebase map; the glossary it maintains is fully code-derived and self-cleaning (`Sources:` anchors, automatic add/redefine/remove, no confirmation)
- `/vibe:changelog` (`skills/changelog/SKILL.md`) — update `CHANGELOG.md` from git history
- `/vibe:docs` (`skills/docs/SKILL.md`) — refresh README managed sections (end-user voice) + developer docs in `docs/`: open-ended file set driven by an aspect inventory, Mermaid diagrams where they help
- `/vibe:release` (`skills/release/SKILL.md`) — bump version, finalize CHANGELOG, commit and tag

**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) (skills are registered/shipped as part of the plugin)
