# Module: skills

**Role:** Slash-command definitions (`/vibe:*`) that drive the vibe-coding workflow — each is an instruction set read by Claude Code when the command is invoked. Shared steps live in one file per concern, read at invocation, never copied.
**Files:** `skills/*/SKILL.md` (one directory per skill), `skills/feature/workflow.md` (shared by `feature` and `fix`)
**Exports:**
- `/vibe:init` (`skills/init/SKILL.md`) — sets up `CLAUDE.md` for vibe coding.
  - Asks once for the project's language; creates `README.md` via `vibe:docs`.
- `/vibe:backlog` (`skills/backlog/SKILL.md`) — lists, adds (single, batch, from review), or removes backlog items.
  - `remove NNN` needs confirmation; done items can't be removed. Commits its own changes.
- `/vibe:clarify` (`skills/clarify/SKILL.md`) — round-by-round interview ending with a `CLARIFY-RESULT:` line parsed by `backlog`, `init`, `workspace-init`.
- `/vibe:feature` (`skills/feature/SKILL.md`) — implements a feature with TDD; free-form brief or backlog `NNN`.
- `/vibe:fix` (`skills/fix/SKILL.md`) — fixes a bug with TDD, reproducing it first; free-form report or backlog `NNN`.
  - Both read `skills/feature/workflow.md`: commit rule, `--auto` gates and verdict, escalation log, backlog resolution, baseline, expert consultation, plan, task list, red/green/runtime/refactor, CHANGELOG, docs, sync, commit, report.
- `/vibe:auto` (`skills/auto/SKILL.md`) — drains the backlog with no human gates.
  - Ranks by unblock count, then fix over feature, then lowest number; one sub-agent per item, sequential.
  - Commits `.vibe/auto-state.md` at every boundary; `--push` invokes `vibe:publish` at the end.
- `/vibe:review` (`skills/review/SKILL.md`) — runs the active review agents in parallel and applies fixes.
  - Owns the finding contract injected into every agent prompt; re-checks the `CLAUDE.md` agent table each run; records `.vibe/last-review.md`.
- `/vibe:sync` (`skills/sync/SKILL.md`) — generates and updates the `.vibe/` codebase map; code-derived, self-cleaning glossary.
- `/vibe:changelog` (`skills/changelog/SKILL.md`) — fills `[Unreleased]` from git history; never cuts a version.
- `/vibe:docs` (`skills/docs/SKILL.md`) — refreshes README managed sections (end users) and `docs/` Markdown files (developers); never touches non-Markdown files in `docs/`.
- `/vibe:release` (`skills/release/SKILL.md`) — checks, runs `changelog`, cuts the version section, refreshes docs, bumps the version, commits and tags. Never pushes.
- `/vibe:workspace-init` (`skills/workspace-init/SKILL.md`) — sets up or refreshes a hub repo (`.git/` + `repos.md`) and the local workspace-root `CLAUDE.md`. Never pushes.
- `/vibe:next-task` (`skills/next-task/SKILL.md`) — picks the next eligible item across a workspace (or the current repo), hands it to `feature`/`fix` or to `auto --push`, publishes, checks downstream unblocks.
- `vibe:tasks` (`skills/tasks/SKILL.md`) — internal: creates the caller's task list via `TaskCreate` or a scratchpad checklist; owns the `●`/`✓` status-line convention.
- `vibe:publish` (`skills/publish/SKILL.md`) — internal: pushes, releases when `[Unreleased]` is non-empty (bump inferred), pushes tags, creates a GitHub release when possible; one self-heal retry on a tracked pre-existing test failure. The only skill that pushes.

**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) (skills are registered/shipped as part of the plugin)
