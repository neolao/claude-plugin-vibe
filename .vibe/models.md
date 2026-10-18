# Data models

No application data models exist in this repo (no database, no request/response types). The structures below are the JSON, frontmatter, and Markdown entry shapes this project defines and consumes.

## Skill frontmatter (`skills/*/SKILL.md`)
| Field | Type | Notes |
|---|---|---|
| name | string | skill slug, matches directory name, invoked as `/vibe:<name>` |
| description | string | one-line purpose, shown in skill listings |
| argument-hint | string | optional — shown as placeholder for `$ARGUMENTS` |
| user-invocable | boolean | optional, default `true` — `false` hides the skill from the `/` menu while leaving it invocable by other skills via the Skill tool; used by `clarify`, `review`, `rewrite`, `report`, `tasks` and `publish` |
Defined in: `skills/*/SKILL.md`

## Agent frontmatter (`agents/*.md`)
| Field | Type | Notes |
|---|---|---|
| name | string | agent slug, matches file name |
| description | string | one-line purpose, used by the review brick to decide activation and by the status line |
| tools | string | review, control and implementer agents — comma-separated allowlist, `Read, Grep, Glob` plus `Bash` for the agents that execute something (`review-tests`, `review-dependencies`, `review-web-security`, `review-comments`, `claim-verifier`), plus `Write, Edit` for `task-implementer` |
| model | string | every agent — a full model id from the ladder in `CLAUDE.md` |
| effort | string | every agent — `low`, `medium` or `high` |
| version | string | every agent and skill — semver, bumped on any behaviour change |
Defined in: `agents/*.md`

## `plugin.json`
| Field | Type | Notes |
|---|---|---|
| name | string | `"vibe"` |
| version | string | semver, bumped by `/vibe:release` |
| description | string | plugin summary |
| author | object | `{ name }` |
| license | string | `"MIT"` |
| keywords | string[] | marketplace search tags |
Defined in: `.claude-plugin/plugin.json`

## `marketplace.json`
| Field | Type | Notes |
|---|---|---|
| name | string | marketplace slug |
| description | string | marketplace summary |
| owner | object | `{ name }` |
| plugins | array | list of `{ name, source, description }` |
Defined in: `.claude-plugin/marketplace.json`

## Backlog item (`.vibe/backlog/NNN-slug.md`)
| Field | Type | Notes |
|---|---|---|
| status | enum | `todo` \| `in_progress` \| `blocked` \| `done` — done items live under `backlog/done/` |
| depends_on | number[] | optional — `NNN` references to other active items |
Title = first `# ` heading of the body. A `blocked` item carries a trailing `## Blocked` section (date + one-line reason) written by an autonomous run; it is never selected by `/vibe:auto`, and running `/vibe:feature NNN`/`/vibe:fix NNN` on it puts it back to `in_progress`. Defined in: `skills/backlog/SKILL.md`, `skills/feature/workflow.md`, `skills/auto/SKILL.md`

## ADR (`.vibe/decisions/NNN-slug.md`)
| Field | Type | Notes |
|---|---|---|
| date | date | YYYY-MM-DD |
| status | string | `accepted`, or `superseded by NNN` — the only permitted mutation |
Body: `# Short title` + **Context** / **Decision** / **Reason** / **Rejected alternatives**. Append-only. Defined in: `skills/feature/SKILL.md`

## Escalation entry (`.vibe/escalations.md`)
Append-only `## [YYYY-MM-DD] /vibe:<skill> — short title` sections with **Context** / **Attempts** / **Diagnosis** / **Status** (`open`, later flippable to `resolved (YYYY-MM-DD)`). Defined in: `skills/feature/workflow.md`

## Auto run state (`.vibe/auto-state.md`)
| Field | Type | Notes |
|---|---|---|
| status | enum | `running` \| `idle` \| `stopped` — `running` on re-invocation means the previous run was interrupted |
| started | datetime | start of the current run |
| limit | number \| `none` | max items for this run, from `$ARGUMENTS` |
| current | number | item in flight; omitted between two items |
| attempt | number | resume attempts on `current`; above 2 the item is marked `blocked` |
Body: append-only `## [timestamp] — run started` sections, one `- NNN — feature\|fix — verdict` line per item. Written and committed at every item boundary — this is what makes a run resumable. Defined in: `skills/auto/SKILL.md`

## Autonomous verdict line (`AUTO-RESULT:`)
Last line of `/vibe:feature`/`/vibe:fix` reports in `--auto` mode, and the only contract between them and `/vibe:auto`: `AUTO-RESULT: done` \| `blocked — [reason]` (item is a dead end, caller moves on) \| `aborted — [reason]` (environment broken, caller stops). Defined in: `skills/feature/workflow.md`

## Glossary entry (`.vibe/glossary.md`)
`## Term` heading + 1–3 sentence code-derived definition + optional `**Do not confuse with:**` + `_Sources:_` line listing the files where the concept lives (drives orphan detection and incremental re-derivation). Defined in: `skills/sync/SKILL.md`

## Task list creation (`skills/tasks/SKILL.md`)
`fix`, `feature`, `docs`, `release`, `init`, and `workspace-init` invoke the internal `vibe:tasks` skill once (Skill tool, task list as `$ARGUMENTS`) instead of calling `TaskCreate` directly. `vibe:tasks` owns the only fallback: if `TaskCreate` is unavailable, it says so and keeps `tasks.tsv` in the scratchpad through `skills/tasks/scripts/tasks.sh` (spec: `skills/tasks/references/model.md`).

## Review finding (agent output contract)
`FILE:` (or `MODULE:`, `PACKAGE:`, `TARGET:` per agent) + `CATEGORY:` (from the agent's `## Categories`) + `SEVERITY:` (`high` \| `medium` \| `low`) + `ISSUE:` + `SUGGESTION:`, with agent-specific extra lines (`EXPLOIT:`, `PROOF:`, `SCALE:`, `CURRENT:`, `ADVISORY:`, `FUNCTION:`/`METRIC:`). Injected verbatim by the `vibe:review` brick into every agent prompt; no per-agent summary line. Defined in: `skills/review/SKILL.md`

## Publish result (`vibe:publish`)
Returned to the caller (`/vibe:auto --push`, `/vibe:next-task`): push result (branch and range, or the Git error), release result (version tagged and pushed, none needed, or why skipped — naming a self-heal item if one ran), forge release (created / skipped / n/a), blockers. Defined in: `skills/publish/SKILL.md`

## Repos registry (`repos.md`, at a hub repo's root)
| Column | Type | Notes |
|---|---|---|
| Repo | string | sibling directory name |
| Status | enum | `active` (candidate for `/vibe:next-task`) \| `planned` (no code yet) \| `idea` (not even a repo yet) |
| Role | string | one-line, never inferred — asked via `AskUserQuestion` when it can't be defaulted |
| Remote | string | Git remote URL, or `—` |
Plus a free-text `## Naming convention` section. Written/refreshed by `/vibe:workspace-init`; read by `/vibe:next-task` to select candidate repos. Its presence alongside `.git/` at a directory's root is the structural marker that identifies a **hub repo** — no fixed name required. Defined in: `skills/workspace-init/SKILL.md`, `skills/next-task/SKILL.md`

## Workspace-root `CLAUDE.md` pointer
A local, never-committed `CLAUDE.md` written by `/vibe:workspace-init` at the workspace root (the parent folder holding sibling repo checkouts — never itself a Git repo). Its `## Hub repo` line names the hub repo's directory; both `workspace-init` (on later runs) and `next-task` read this pointer instead of re-scanning siblings, falling back to a scan only when the pointer is missing or its target no longer carries the hub repo marker. Defined in: `skills/workspace-init/SKILL.md`, `skills/next-task/SKILL.md`

## Inter-brick contracts (build loop)

Each is parsed by heading; the defining file is the source.

| Contract | Producer → consumer | Shape | Defined in |
|---|---|---|---|
| `CLARIFY-RESULT` | `clarify` → `backlog`, `init`, `workspace-init`, `workflow.md` | `settled[ — mode: need\|implementation]` / `partial — spike: <q>` / `partial — <open>` / `abandoned`, then `### Synthesis`, `### Decisions made` (priority, optional `(source: …)`) | `skills/clarify/SKILL.md` |
| `## REVIEW agents` / `## REVIEW flipped rows` / `## REVIEW findings` | `review` brick → `workflow.md` | raw findings in the FILE/CATEGORY/SEVERITY/ISSUE/SUGGESTION format, each preceded by `AGENT:` | `skills/review/SKILL.md` |
| `## REQUIREMENTS findings` | `requirements-reviewer` → `workflow.md` | `(gap)`, `(addition)`, `(constraint)`, `(ambiguity)` bullets, or `none` | `agents/requirements-reviewer.md` |
| `## CLASSIFIED findings` / `## DISCARDED` / `## DOUBTS` | `review-classifier` → `workflow.md` | `(level · space)` bullets with **Consequence** and **Raised by**; dropped/merged with reason; doubts with recommended option | `agents/review-classifier.md` |
| `## CLAIMS findings` | `claim-verifier` → `workflow.md` | `(unproven)`, `(contradicted)`, `(conclusion)` bullets, or `none` | `agents/claim-verifier.md` |
| `## IMPLEMENTATION report` | `task-implementer` → `workflow.md` | **Sub-task**, **Files changed**, **Commands run** (red run before green), **Findings handled**, **Doubts** | `agents/task-implementer.md` |
| `✍️ Rewrite — … applied directly` | `rewrite` (direct) → `workflow.md` | the rewritten text, questions to the author, the closing block | `skills/rewrite/SKILL.md` |
| counters file `<scratchpad>/report.tsv` and `.vibe/reports/<timestamp>-<entry>.md` | `report` script | TSV `key\tvalue`; report = YAML frontmatter of the allowed counters plus `bricks:` | `skills/report/scripts/report.sh` |
