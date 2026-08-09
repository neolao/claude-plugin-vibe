# Module: skills

**Role:** Slash-command definitions (`/vibe:*`) that drive the vibe-coding workflow — each is a self-contained instruction set read by Claude Code when the command is invoked.
**Files:** `skills/*/SKILL.md` (one directory per skill)
**Exports:**
- `/vibe:init` (`skills/init/SKILL.md`) — initialize/regenerate `CLAUDE.md` for vibe coding, including a language question (documentation, backlog items, comments) recorded in a `## Project language` section; also ensures `README.md` exists and has its standard managed sections, by delegating to `vibe:docs` rather than writing README content itself
- `/vibe:backlog` (`skills/backlog/SKILL.md`) — list, add, or remove (`remove NNN`, confirmation required, done items excluded) feature backlog items, committing each creation/removal itself
- `/vibe:feature` (`skills/feature/SKILL.md`) — implement a new feature via TDD (free-form description or backlog reference `NNN`), verify it for real via the native `run` skill (assume-it's-broken posture), update CHANGELOG
- `/vibe:fix` (`skills/fix/SKILL.md`) — fix a bug via TDD (reproduce first; free-form description or backlog reference `NNN`), verify it for real via the native `run` skill (assume-it's-broken posture), update CHANGELOG
- `/vibe:auto` (`skills/auto/SKILL.md`) — drain the backlog autonomously: selects eligible items, runs each one through `vibe:feature`/`vibe:fix` in `--auto` mode inside a dedicated sub-agent, persists and commits its state at every item boundary so any interruption is resumed on the next invocation
- `/vibe:review` (`skills/review/SKILL.md`) — orchestrate multi-agent code quality review, re-checking the CLAUDE.md agent activation table against the current project state at each run (deliberate opt-outs respected), recording each run in `.vibe/last-review.md`
- `/vibe:sync` (`skills/sync/SKILL.md`) — generate/update `.vibe/` codebase map; the glossary it maintains is fully code-derived and self-cleaning (`Sources:` anchors, automatic add/redefine/remove, no confirmation)
- `/vibe:changelog` (`skills/changelog/SKILL.md`) — update `CHANGELOG.md` from git history
- `/vibe:docs` (`skills/docs/SKILL.md`) — refresh README managed sections (end-user voice) + developer docs in `docs/`: open-ended file set driven by an aspect inventory, Mermaid diagrams where they help
- `/vibe:release` (`skills/release/SKILL.md`) — bump version, finalize CHANGELOG, commit and tag
- `/vibe:workspace-init` (`skills/workspace-init/SKILL.md`) — bootstrap/refresh a hub repo (structural marker: `.git/`+`repos.md` at its root, no fixed name) tracking every sibling repo in `repos.md`, plus a local never-committed workspace-root `CLAUDE.md`; commits inside the hub repo only, never pushes
- `/vibe:next-task` (`skills/next-task/SKILL.md`) — pick the next eligible backlog item across every `active` repo in a workspace (or within the current repo alone if no workspace is detected), hand it to `vibe:feature`/`vibe:fix`/`vibe:auto`, then push and — if the changelog warrants it — release; the only skill in the plugin that pushes/publishes on its own
- `vibe:tasks` (`skills/tasks/SKILL.md`) — internal, `user-invocable: false`: creates a task list for the invoking skill via `TaskCreate`, or falls back to a scratchpad checklist if that tool is unavailable; invoked by `init`, `feature`, `fix`, `review`, `docs`, `release`, and `workspace-init`, never directly by users

**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) (skills are registered/shipped as part of the plugin)
