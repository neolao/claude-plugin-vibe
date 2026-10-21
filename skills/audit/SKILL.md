---
name: audit
description: Audit an existing codebase — runs the active review agents on the whole repo (or a path), has the findings classified, reports them by level, then turns the ones you pick into backlog items; fixes nothing. For taking over a project or a periodic health check
argument-hint: "[optional: a path to restrict the audit; empty audits the whole codebase]"
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:audit — Codebase Audit

`feature` and `fix` only review their own diff: debt already in the code stays invisible. Audit the whole codebase (or a path), report what holds, and queue the work as backlog items. Detect and plan only: no code is modified, nothing is written before the user validates.

Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — Scope

`$ARGUMENTS` is a path, or empty for the full codebase. A path that does not exist: say so and stop. No `CLAUDE.md` with a `## Review agents` table: tell the user to run `/vibe:init` first and stop.

## Step 2 — Review

Invoke `vibe:review` with the scope (no `mode: internal` line). It runs the agents the `CLAUDE.md` table activates, in parallel; the opt-in ones (`review-ddd`, `review-alternative-design`, dynamic `review-web-security`) run only if the table already marks them ✅. Before launching, tell the user which agents run, since the cost grows with the codebase.

Keep its `REVIEW flipped rows` for Step 6.

## Step 3 — Classify

Launch `vibe:findings-classifier` with every raw finding, the type of deliverable "code", the working directory, and as the request: "no request — judge each finding against the project's `CLAUDE.md` conventions and its `.vibe/` map". An agent that failed is relaunched once; a second failure is reported, not skipped.

Its `DOUBTS` are asked to the user, one question each with the recommended option; each answer reclassifies the finding it was about.

## Step 4 — Report

Present the kept findings by level (high, then medium), grouped by theme (architecture, security, robustness, tests, hygiene…), each with `path:line`, its consequence and a fix direction. Low findings come last, as a short list. Add the counts: kept, dropped, merged. Pass the text through `vibe:rewrite` with `mode: direct` before showing it.

## Step 5 — Backlog

Propose backlog items for the high and medium findings, **grouped by cause** — several findings with one fix are one item. Low findings never become items. The user picks which to create, and can edit titles.

Nothing picked: write nothing. Otherwise invoke `vibe:backlog` with the picked items as a batch (it numbers, writes and commits them).

## Step 6 — Close

If `vibe:review` flipped rows of the `CLAUDE.md` agent table, list them and commit `CLAUDE.md` alone: `chore: update review agents table`.

End with:

```
---
🔎 Audit — <n> finding(s) kept (<high> high, <medium> medium, <low> low), <m> backlog item(s) created
---
```
