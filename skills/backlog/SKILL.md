---
name: backlog
description: Manage the feature backlog — list tasks, add one or several items (including from the last review), or remove an item
argument-hint: "[feature description to add] | <multi-line list> | from review | remove NNN | (empty to list all)"
---

# /vibe:backlog — Feature Backlog Manager

Manage `.vibe/backlog/`: one Markdown file per item, `NNN-slug.md`, with a `status` frontmatter (`todo`, `in_progress`, `blocked`, `done`). `blocked` is set by an autonomous `--auto` run that hit a dead end; the reason is in a `## Blocked` section at the end of the file. Done items live in `done/`.

Every user-facing message is written in the conversation's language. If this skill creates files and stops before its report, commit them as `wip: [short description]` first.

## Step 1 — Mode

| `$ARGUMENTS` | Mode |
|---|---|
| empty | **List** (Step 2) |
| intent to delete or cancel + a reference matching `^\d+(-[\w-]+)?$` ("remove 3", "delete 003-oauth", "supprime 12") | **Remove** (Step 3) |
| intent to create items from the last review ("from review", "from the review findings", "depuis le review") | **From review** (Step 4) |
| several entries — newline-, bullet-, or number-separated list | **Batch** (Step 5) |
| plain prose | **Single** (Step 6) |

## Step 2 — List

No top-level `*.md` in `.vibe/backlog/` → "The backlog is empty — no active items in `.vibe/backlog/`." and stop.

Otherwise, for each top-level file (sorted): `status`, title (first `# ` heading), and unmet dependencies — every `depends_on` number whose item (top level or `done/`) is not `done`. Display:

| # | Title | Status | Blocked by |
|---|---|---|---|
| 002 | Export as CSV | `todo` | — |
| 003 | Dark mode | `todo` | ⚠ 002 |

Then: "N item(s) done — see `.vibe/backlog/done/`." if `done/` has files; for each `blocked` item, its number and `## Blocked` reason, plus that running `/vibe:feature NNN` (or `/vibe:fix NNN`) puts it back in play; and the review cadence — if `.vibe/last-review.md` exists, its date and the number of `feat:`/`fix:` commits since its hash, otherwise "No review recorded yet — running `/vibe:review` will establish the baseline." Stop.

## Step 3 — Remove

Zero-pad the number; look for `NNN-*.md` at the top level only. Found in `done/` instead → "Item `NNN` is already done — done items are kept as history and cannot be removed."; not found → "No backlog item `NNN` found in `.vibe/backlog/`. Run `/vibe:backlog` to list existing items." Read its title and status, find the active items whose `depends_on` lists `NNN`, and ask for confirmation showing number, title, status (warn if `in_progress`), and the dependents. On confirmation: `git rm` the file, drop `NNN` from each dependent's `depends_on` (removing the line if empty), commit `chore: remove backlog item NNN - [Title]`, and report the file, the cleaned dependents, and the commit. Stop.

## Step 4 — From review

Find the most recent `/vibe:review` report in the conversation. None → "No review output found in the current conversation. Run `/vibe:review` first, or provide a list of items directly." Otherwise take every finding under "Remaining findings" (all severities; "Applied fixes" are resolved), write each as a one-line description with its location, and continue as a batch (Step 5).

## Step 5 — Batch

Split `$ARGUMENTS` into one description per entry (list markers stripped, blank lines dropped). Show a preview table (`#`, `Title`) of what will be created, then create each item with Steps 7–9, recomputing the next number after each file. One commit for the whole run (Step 10), then the report (Step 11).

## Step 6 — Single: scope and clarity

- **Oversized scope** — the description bundles several independently shippable capabilities ("add CSV export, a dark mode, and email notifications"), as opposed to one capability with several facets ("export as CSV or PDF"): ask "This description seems to cover several distinct features: [candidate titles]. Do you want me to create a separate item for each?" — yes → treat the titles as a batch (Step 5); no → continue as one item.
- **Under-specified** — a vague noun phrase or slogan with no concrete actor, action, or observable outcome ("a notification", "improve performance"), as opposed to short but complete ("let users export the current report as a CSV file"): say "This description is too thin to produce solid acceptance criteria — I'll ask a few questions first.", invoke the `vibe:clarify` skill with `$ARGUMENTS`, and on `settled`/`partial` use its `### Synthesis` as the description for the rest of the run; on `abandoned` keep the original — never block creation on a clarification the user declined.

Then Steps 7–11.

## Step 7 — Next number

Highest `NNN` prefix across `.vibe/backlog/` **and** `done/`, plus one, zero-padded to 3 digits; `001` when there is none.

## Step 8 — Title, slug, criteria, dependencies

Title: 3–7 words, title case, taken or summarized from the description. Slug: kebab-case of the title. 2–4 acceptance criteria, each specific, observable, and falsifiable, from the user's or system's perspective ("User can…", "System returns…") — never "works correctly". Dependencies: another item named by number ("after 003") or by a matching title goes into `depends_on` as zero-padded numbers; when uncertain, omit the field.

## Step 9 — Write the file

```markdown
---
status: todo
depends_on: [003, 005]   # only when dependencies were found; omit the line otherwise
---
# [Title]

## Description
[What needs to be built and why — 1–3 short, plain sentences]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Notes
[Constraints, technical context, open questions — or "None."]
```

## Step 10 — Commit

Single item: `chore: add backlog item NNN - [Title]`. Batch or from-review: one commit `chore: add N backlog items`, titles listed in the body.

## Step 11 — Report

Short and plain. Single: file, title, number of criteria, commit, and the next step (`/vibe:feature NNN`, or `/vibe:fix NNN` for a bug). Batch: a table `# | File | Title | Criteria`, the total, the commit, and the same next step.
