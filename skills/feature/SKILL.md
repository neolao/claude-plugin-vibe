---
name: feature
description: Implement a new feature using TDD, then update CHANGELOG.md under [Unreleased] > Added
argument-hint: <feature description in natural language>
---

# /vibe:feature — TDD Feature Implementation

Implement the feature described in `$ARGUMENTS`: the user is the Product Owner only and never tests code manually.

**First read `workflow.md` next to this file** (`${CLAUDE_PLUGIN_ROOT}/skills/feature/workflow.md`) — the shared implementation workflow: standing commit rule, `--auto` mode and its verdict line, escalation log, backlog resolution, baseline check, expert consultation, plan presentation, task list, red/green/runtime/refactor loop, CHANGELOG, docs, sync, commit, report. This file only defines what is specific to a feature. Prefix: `feat:`.

## Step 1 — Understand the requirement

Resolve `$ARGUMENTS` (backlog reference or free-form brief), read the project context, and settle terminology, as the workflow describes. Then:

- **Duplicate check** — compare the brief against the titles of the active backlog items (`.vibe/backlog/*.md`) and the `[Unreleased]` entries of `CHANGELOG.md`, looking for the same capability under another wording. If one matches, quote it and ask "This feature seems to already exist (`<match>`). Is this really a new, distinct feature?" — proceed only on confirmation.
- **Design challenge** — if the feature contradicts an established pattern in `.vibe/modules/` or `.vibe/index.md` (a new module that belongs in an existing one), challenge the approach before implementing. If the requirement is ambiguous on a point that leads to fundamentally different implementations, ask one question.
- **Scope check** — if the brief bundles several independently shippable capabilities ("add CSV export, a dark mode, and email notifications"), as opposed to one feature with several technical sub-tasks, propose a split: "This request seems to cover several distinct features: [candidate titles]. Do you want me to split it into separate tasks?" On confirmation, invoke `vibe:backlog` with the titles as a batch, report the created items, and stop. On refusal, implement as one feature.

Then run the baseline check.

## Step 2 — Plan

After expert consultation, present the plan covering: what will be built (functionally), what existing behaviour it affects, what will be tested (user actions and expected results: the normal case, a couple of edge cases, what happens when something goes wrong), how it will be exercised for real once built, and the assumptions.

Once approved, if the plan contains a non-obvious design decision (a choice between valid approaches, a deliberate deviation from existing patterns), record it as `.vibe/decisions/NNN-slug.md` — next number after the highest existing `NNN` (or `001`), kebab-case slug, one or two plain sentences per field:

```markdown
---
date: YYYY-MM-DD
status: accepted
---
# [Short title]
**Context:** [what was being built]
**Decision:** [what was decided]
**Reason:** [why]
**Rejected alternatives:** [what was considered and rejected]
```

ADR files are append-only. A new decision that replaces an old one gets a new file; the old file's frontmatter becomes `status: superseded by NNN` — the only permitted mutation.

Task list: one group per development sub-task, labelled `[<SubTask>]` (`[Feature]` for a single unit of work), then the closing tasks.

## Steps 3–5 — Red, green, runtime, refactor

Tests for each sub-task cover the nominal path, at least 2 edge cases, and the error path (invalid input, missing data, failure). Follow the workflow loop.

## Steps 6–8 — CHANGELOG, docs, sync, commit

CHANGELOG section: `### Added`. Docs condition: the feature is visible to the end user. Commit with `feat:`.

## Step 9 — Report

What was implemented (1–2 sentences); test results (X passing, covering nominal / edge / error paths); lint status; the changelog entry; assumptions; experts consulted (domain and one notable requirement each); then the workflow's pre-existing-failures and review-cadence lines.
