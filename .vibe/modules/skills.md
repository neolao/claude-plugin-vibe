# Module: skills

**Role:** Slash-command definitions (`/vibe:*`) that drive the vibe-coding workflow — each is a self-contained instruction set read by Claude Code when the command is invoked.
**Files:** `skills/*/SKILL.md` (one directory per skill)
**Exports:**
- `/vibe:init` (`skills/init/SKILL.md`) — sets up `CLAUDE.md` for vibe coding.
  - Asks once for the project's documentation language.
  - Also creates `README.md` with its managed sections, via `vibe:docs`.
- `/vibe:backlog` (`skills/backlog/SKILL.md`) — lists, adds, or removes backlog items.
  - `remove NNN` needs confirmation; done items can't be removed.
  - Commits each creation or removal itself.
- `/vibe:feature` (`skills/feature/SKILL.md`) — implements a feature with TDD.
  - Accepts a free-form description or a backlog reference `NNN`.
  - Verifies the result for real via the `run` skill.
  - Updates the CHANGELOG.
- `/vibe:fix` (`skills/fix/SKILL.md`) — fixes a bug with TDD, reproducing it first.
  - Accepts a free-form description or a backlog reference `NNN`.
  - Verifies the fix for real via the `run` skill.
  - Updates the CHANGELOG.
- `/vibe:auto` (`skills/auto/SKILL.md`) — drains the backlog with no human gates.
  - Picks the next item by unblock count, then fix-over-feature, then lowest number.
  - Runs each item through `vibe:feature`/`vibe:fix` in a sub-agent.
  - Saves and commits its state after every item, so an interruption can resume.
  - Prints one `●`/`✓`/`⚠` status line per item.
- `/vibe:review` (`skills/review/SKILL.md`) — runs multi-agent code quality review.
  - Re-checks the active agent list in `CLAUDE.md` on every run; respects opt-outs.
  - Records each run in `.vibe/last-review.md`.
- `/vibe:sync` (`skills/sync/SKILL.md`) — generates and updates the `.vibe/` codebase map.
  - The glossary it maintains is fully derived from code and self-cleaning.
- `/vibe:changelog` (`skills/changelog/SKILL.md`) — updates `CHANGELOG.md` from git history.
- `/vibe:docs` (`skills/docs/SKILL.md`) — refreshes README managed sections and `docs/`.
  - README sections are written for end users; `docs/` files for developers.
  - `docs/` is an open-ended set of files, chosen per project, with diagrams where useful.
- `/vibe:release` (`skills/release/SKILL.md`) — bumps the version, finalizes the CHANGELOG, commits and tags.
- `/vibe:workspace-init` (`skills/workspace-init/SKILL.md`) — sets up or refreshes a hub repo.
  - A hub repo is any directory with `.git/` and `repos.md` at its root — no fixed name.
  - Tracks every sibling repo in `repos.md`, plus a local, never-committed workspace-root `CLAUDE.md`.
  - Commits inside the hub repo only; never pushes.
- `/vibe:next-task` (`skills/next-task/SKILL.md`) — picks and ships the next eligible backlog item.
  - Scans every `active` repo in a workspace, or just the current repo if there is no workspace.
  - Hands the item to `vibe:feature`/`vibe:fix`, directly or repeatedly in auto mode.
  - Pushes, and releases if the changelog warrants it — the only skill in the plugin that publishes on its own.
- `vibe:tasks` (`skills/tasks/SKILL.md`) — internal, not shown in the `/` menu.
  - Creates the task list for the invoking skill, via `TaskCreate` or a scratchpad checklist fallback.
  - Owns the `●`/`✓` status-line convention used on every task transition.

**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) (skills are registered/shipped as part of the plugin)
