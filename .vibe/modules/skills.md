# Module: skills

**Role:** Slash-command definitions (`/vibe:*`) that drive the vibe-coding workflow — each is an instruction set read by Claude Code when the command is invoked. Shared steps live in one file per concern, read at invocation, never copied.
**Files:** `skills/*/SKILL.md` (one directory per skill), `skills/feature/workflow.md` (shared by `feature` and `fix`), `skills/*/references/*.md` (grids and rule sets read at invocation), `skills/tasks/scripts/tasks.sh` (the task-file script of the `tasks` fallback), `skills/report/scripts/report.sh` (the counters and writer of `report`)
**Exports:**
- `/vibe:init` (`skills/init/SKILL.md`) — sets up `CLAUDE.md` for vibe coding.
  - Asks once for the project's language; creates `README.md` via `vibe:docs`.
- `/vibe:backlog` (`skills/backlog/SKILL.md`) — lists, adds (single, batch, from review), or removes backlog items.
  - `remove NNN` needs confirmation; done items can't be removed. Commits its own changes.
- `vibe:clarify` (`skills/clarify/SKILL.md`) — internal: round-by-round interview ending with a `CLARIFY-RESULT:` line parsed by `backlog`, `init`, `workspace-init`; `mode: need` / `mode: implementation` for the build workflow, each with its own sources read before asking, sourced self-answers (`(source: …)`), `partial — spike: <question>` when an answer must be searched or tried.
  - Every settled decision carries a priority (`🔒 MUST` / `⚖️ SHOULD` / `✨ NICE`, asked, never defaulted); the tree persists in `<scratchpad>/clarify-tree.md`; a contradicting answer reopens a settled decision.
- `/vibe:challenge` (`skills/challenge/SKILL.md`) — one devil's-advocate sub-agent against a settled decision; every objection reported with an opinion; closes with `⚔️ Challenge — …`.
- `/vibe:consult` (`skills/consult/SKILL.md`) — one precise question to one `vibe:expert-*` agent (architecture by default); closes with `🏛️ Expert <domain> — …`.
- `/vibe:feature` (`skills/feature/SKILL.md`) — implements a feature with TDD; free-form brief or backlog `NNN`.
- `/vibe:fix` (`skills/fix/SKILL.md`) — fixes a bug with TDD, reproducing it first; free-form report or backlog `NNN`.
  - Both read `skills/feature/workflow.md`: commit rule, `--auto` gates and verdict (framing rounds, spikes, classifier doubts, scope drift, requirement conflicts), escalation log, usage report (`vibe:report`), backlog resolution, baseline, need framing (`vibe:clarify mode: need`), expert consultation (`expert-architecture` on a real design choice), implementation framing (`mode: implementation`), plan, scope drift check, task list, red/green/runtime/refactor (re-runs the baseline's build command too, blocking Commit exactly like a failing test), internal review (`vibe:review` + `requirements-reviewer` → `review-classifier` → back to a framing or on), CHANGELOG, docs, sync, commit, final checks (`claim-verifier`, `rewrite` direct), report, `vibe:report write`, `debrief`.
- `/vibe:auto` (`skills/auto/SKILL.md`) — drains the backlog with no human gates.
  - Ranks by unblock count, then fix over feature, then lowest number; one sub-agent per item, sequential.
  - Commits `.vibe/auto-state.md` at every boundary; `--push` invokes `vibe:publish` at the end.
- `vibe:review` (`skills/review/SKILL.md`) — internal brick: runs the active review agents in parallel on a scope (`internal <changed files>`) and returns their raw findings under `## REVIEW agents` / `## REVIEW flipped rows` / `## REVIEW findings`; no merge, no fix, no commit.
  - Owns the finding contract injected into every agent prompt; re-checks the `CLAUDE.md` agent table each run and lists the flipped rows (the caller commits).
- `/vibe:debrief` (`skills/debrief/SKILL.md`) — 1–3 retrospective questions, lessons written to the project memory directory; closes with `📝 Debrief — …`.
- `vibe:rewrite` (`skills/rewrite/SKILL.md`) — internal: clarity rework by named rules with a meaning-preservation sub-agent; `mode: direct` (first line of the arguments) returns the rewritten text with no table, no question and no file written, for a workflow handing over text it just produced; closes with `✍️ Rewrite — …`.
- `/vibe:learn` (`skills/learn/SKILL.md`) — a correction stated in general terms becomes one line in `~/.claude/rules/vibe-{preferences,workflow,technical}.md`, after confirmation; closes with a `🗒 […]` line.
- `/vibe:sync` (`skills/sync/SKILL.md`) — generates and updates the `.vibe/` codebase map; code-derived, self-cleaning glossary.
- `/vibe:changelog` (`skills/changelog/SKILL.md`) — fills `[Unreleased]` from git history; never cuts a version.
- `/vibe:docs` (`skills/docs/SKILL.md`) — refreshes README managed sections (end users) and `docs/` Markdown files (developers); never touches non-Markdown files in `docs/`.
- `/vibe:release` (`skills/release/SKILL.md`) — pre-release checks (test, lint, build), runs `changelog`, cuts the version section, refreshes docs, bumps the version, commits and tags. Never pushes.
- `/vibe:workspace-init` (`skills/workspace-init/SKILL.md`) — sets up or refreshes a hub repo (`.git/` + `repos.md`) and the local workspace-root `CLAUDE.md`. Never pushes.
- `/vibe:next-task` (`skills/next-task/SKILL.md`) — picks the next eligible item across a workspace (or the current repo), hands it to `feature`/`fix` or to `auto --push`, publishes, checks downstream unblocks.
- `vibe:tasks` (`skills/tasks/SKILL.md`) — internal: creates the caller's task list via `TaskCreate` or, without it, a `tasks.tsv` in the scratchpad kept by `scripts/tasks.sh` (same model and rules as the native system: ids, statuses, `blockedBy`, `owner`; refuses a skipped transition); `file:` option for a dedicated list; owns the `●`/`✓` status-line convention; "Going back" rule for a looping caller (current task completed, pending tasks abandoned with `✗ … — stale`, new round prefixed `Round <n> — `; `abandon` command in the script).
- `vibe:report` (`skills/report/SKILL.md`) — internal: counts a workflow's events through `scripts/report.sh` (`init`, `incr <key>`, `brick <name>`, `write`) and writes a statistics-only report to `.vibe/reports/<timestamp>-<entry>.md` in the project; the directory ignores itself in git; the report stays local unless the user shares it. Refuses an unknown entry, counter or brick name.
- `vibe:publish` (`skills/publish/SKILL.md`) — internal: pushes, releases when `[Unreleased]` is non-empty (bump inferred), pushes tags, verifies the pushed commit's CI/deploy run (best-effort, GitHub only) and surfaces a failure as a blocker, creates a GitHub release when possible; one self-heal retry on a tracked pre-existing test failure. The only skill that pushes.

**Depends on:** [`modules/plugin-manifest.md`](plugin-manifest.md) (skills are registered/shipped as part of the plugin)
