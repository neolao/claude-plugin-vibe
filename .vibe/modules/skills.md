# Module: skills

**Role:** Slash-command definitions (`/vibe:*`) that drive the vibe-coding workflow — each is a self-contained instruction set read by Claude Code when the command is invoked.
**Files:** `skills/*/SKILL.md` (one directory per skill)
**Exports:**
- `/vibe:init` (`skills/init/SKILL.md`) — initialize/regenerate `CLAUDE.md` for vibe coding
- `/vibe:backlog` (`skills/backlog/SKILL.md`) — list or add feature backlog items
- `/vibe:feature` (`skills/feature/SKILL.md`) — implement a new feature via TDD, verify it for real via the native `verify` skill (assume-it's-broken posture), update CHANGELOG
- `/vibe:fix` (`skills/fix/SKILL.md`) — fix a bug via TDD (reproduce first), verify it for real via the native `verify` skill (assume-it's-broken posture), update CHANGELOG
- `/vibe:review` (`skills/review/SKILL.md`) — orchestrate multi-agent code quality review
- `/vibe:review-web-security` (`skills/review-web-security/SKILL.md`) — audit web app for exploitable vulnerabilities (fork context)
- `/vibe:sync` (`skills/sync/SKILL.md`) — generate/update `.vibe/` codebase map
- `/vibe:changelog` (`skills/changelog/SKILL.md`) — update `CHANGELOG.md` from git history
- `/vibe:docs` (`skills/docs/SKILL.md`) — refresh README managed sections + `docs/`
- `/vibe:release` (`skills/release/SKILL.md`) — bump version, finalize CHANGELOG, commit and tag

**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) (skills are registered/shipped as part of the plugin)
