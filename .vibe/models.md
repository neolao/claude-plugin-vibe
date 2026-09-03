# Data models

No application data models exist in this repo (no database, no request/response types). The structures below are the JSON, frontmatter, and Markdown entry shapes this project defines and consumes.

## Skill frontmatter (`skills/*/SKILL.md`)
| Field | Type | Notes |
|---|---|---|
| name | string | skill slug, matches directory name, invoked as `/vibe:<name>` |
| description | string | one-line purpose, shown in skill listings |
| argument-hint | string | optional — shown as placeholder for `$ARGUMENTS` |
| user-invocable | boolean | optional, default `true` — `false` hides the skill from the `/` menu while leaving it invocable by other skills via the Skill tool; used by `skills/tasks/SKILL.md` and `skills/publish/SKILL.md` |
Defined in: `skills/*/SKILL.md`

## Agent frontmatter (`agents/*.md`)
| Field | Type | Notes |
|---|---|---|
| name | string | agent slug, matches file name |
| description | string | one-line purpose, used by `/vibe:review` to decide activation and by the status line |
| tools | string | review agents only — comma-separated allowlist, `Read, Grep, Glob` plus `Bash` for the three agents that execute something |
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
Append-only `## [YYYY-MM-DD] /vibe:<skill> — short title` sections with **Context** / **Attempts** / **Diagnosis** / **Status** (`open`, later flippable to `resolved (YYYY-MM-DD)`). Defined in: `skills/feature/workflow.md`, `skills/review/SKILL.md`

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
`fix`, `feature`, `review`, `docs`, `release`, `init`, and `workspace-init` invoke the internal `vibe:tasks` skill once (Skill tool, task list as `$ARGUMENTS`) instead of calling `TaskCreate` directly. `vibe:tasks` owns the only fallback: if `TaskCreate` is unavailable, it says so and writes a Markdown checklist to `task-list.md` in the scratchpad; every later task transition in the calling skill goes through the mechanism it selected. Defined in: `skills/tasks/SKILL.md`

## Review finding (agent output contract)
`FILE:` (or `MODULE:`, `PACKAGE:`, `TARGET:` per agent) + `CATEGORY:` (from the agent's `## Categories`) + `SEVERITY:` (`high` \| `medium` \| `low`) + `ISSUE:` + `SUGGESTION:`, with agent-specific extra lines (`EXPLOIT:`, `PROOF:`, `SCALE:`, `CURRENT:`, `ADVISORY:`, `FUNCTION:`/`METRIC:`). Injected verbatim by `/vibe:review` into every agent prompt; no per-agent summary line. Defined in: `skills/review/SKILL.md`

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
