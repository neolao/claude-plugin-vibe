# Data models

No application data models exist in this repo (no database, no request/response types). The structures below are the JSON, frontmatter, and Markdown entry shapes this project defines and consumes.

## Skill frontmatter (`skills/*/SKILL.md`)
| Field | Type | Notes |
|---|---|---|
| name | string | skill slug, matches directory name, invoked as `/vibe:<name>` |
| description | string | one-line purpose, shown in skill listings |
| argument-hint | string | optional — shown as placeholder for `$ARGUMENTS` |
Defined in: `skills/*/SKILL.md`

## Agent frontmatter (`agents/*.md`)
| Field | Type | Notes |
|---|---|---|
| name | string | agent slug, matches file name |
| description | string | one-line purpose, used by `/vibe:review` to decide activation and by the status line |
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
| status | enum | `todo` \| `in_progress` \| `done` — done items live under `backlog/done/` |
| depends_on | number[] | optional — `NNN` references to other active items |
Title = first `# ` heading of the body. Defined in: `skills/backlog/SKILL.md`

## ADR (`.vibe/decisions/NNN-slug.md`)
| Field | Type | Notes |
|---|---|---|
| date | date | YYYY-MM-DD |
| status | string | `accepted`, or `superseded by NNN` — the only permitted mutation |
Body: `# Short title` + **Context** / **Decision** / **Reason** / **Rejected alternatives**. Append-only. Defined in: `skills/feature/SKILL.md`

## Escalation entry (`.vibe/escalations.md`)
Append-only `## [YYYY-MM-DD] /vibe:<skill> — short title` sections with **Context** / **Attempts** / **Diagnosis** / **Status** (`open`, later flippable to `resolved (YYYY-MM-DD)`). Defined in: `skills/feature/SKILL.md`, `skills/fix/SKILL.md`, `skills/review/SKILL.md`

## Glossary entry (`.vibe/glossary.md`)
`## Term` heading + 1–3 sentence code-derived definition + optional `**Do not confuse with:**` + `_Sources:_` line listing the files where the concept lives (drives orphan detection and incremental re-derivation). Defined in: `skills/sync/SKILL.md`
