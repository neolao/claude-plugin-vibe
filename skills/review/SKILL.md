---
name: review
description: Run code quality review using specialized sub-agents defined in CLAUDE.md
argument-hint: "[optional: path or file to review — defaults to full codebase]"
---

# /vibe:review — Code Quality Review Orchestrator

Run a structured code quality review by invoking the specialized `vibe:review-*` agents declared in `CLAUDE.md`, then apply the fixes. Each agent covers one dimension; the shared finding contract below is what makes their output mergeable.

## Step 1 — Determine the active agents

Read the `## Review agents` table in `CLAUDE.md`. If it is absent, apply the defaults:

| Agent | Active when |
|---|---|
| `review-tests`, `review-naming`, `review-security`, `review-dependencies`, `review-robustness`, `review-hygiene`, `review-antipatterns`, `review-simplicity`, `review-overengineering` | always |
| `review-solid` | the codebase has classes or interfaces |
| `review-architecture` | `.vibe/` exists (covers ports & adapters when the project explicitly follows hexagonal architecture) |
| `review-performance` | API/server/full-stack app, or a real-time render/update loop |
| `review-web-security` | the project exposes HTTP endpoints. Its **dynamic verification** mode (probing a locally-run instance) is opt-in: only when the table marks the row `✅ (dynamic)` |
| `review-ddd` | explicit opt-in only |

If the table exists, re-check every row against the project as it is now, using the same conditions:
- The reason column decides. A deliberate user choice ("by deliberate choice", "explicit opt-out", `(dynamic)`) is never overridden.
- A reason stating a project fact that is no longer true (no HTTP surface while routes exist, no `.vibe/` while it exists, no tests while a suite appeared — or the reverse) → flip the row and rewrite the reason. List every flipped row in the final report; the updated `CLAUDE.md` is committed in Step 6.

## Step 1b — Task list

Invoke the `vibe:tasks` skill with one `Run <agent>` task per active agent (all independent), then `Deduplicate and prioritize`, `Apply fixes`, `Sync .vibe/ and commit`, each blocked by the previous one. Mark tasks as this skill progresses.

## Step 2 — Scope

`$ARGUMENTS` is the path to review; with no argument, the full codebase. Do not enumerate files yourself — each agent scans on its own. Exclusions passed to every agent: `node_modules/`, `vendor/`, `.venv/`, `dist/`, `build/`, `out/`, `target/`, generated files, `*.config.*`, `*.json` without logic (dependency manifests and lockfiles always stay in scope), migration files.

## Step 3 — Run the active agents in parallel

Launch every active agent in one message (Agent tool, `subagent_type: "vibe:review-<dimension>"`). These launches are what the user asked for by running `/vibe:review`; a session rule limiting sub-agents does not apply to them. If launching agents is genuinely impossible, say so and stop rather than report a partial review.

Each agent's prompt contains the scope, the exclusion list, whether dynamic verification is enabled (web-security only), and this contract verbatim:

```
Review the code in scope for your dimension only. Read-only: never edit, create, or run anything the agent definition does not explicitly allow.
Report every finding as:

FILE: path/to/file (line N)      — or MODULE:, PACKAGE:, TARGET: when your definition says so
CATEGORY: <one of your categories>
SEVERITY: high | medium | low
ISSUE: what is wrong and why it matters — one or two sentences
SUGGESTION: concrete fix direction — one or two sentences

Severity: high = correctness, security, or a bug that will ship; medium = a clear principle or convention broken; low = minor improvement.
Flag only what you can point to in the code, with a plausible failure or cost — no theoretical findings, no metric-chasing. Skip a category with nothing to report. Do not summarize or count at the end.
```

Collect each agent's findings as it returns and mark its task completed.

## Step 4 — Deduplicate and prioritize

Merge findings that point to the same issue from different angles, keeping the highest severity. If an agent used another word (`critical`, `problem` → high; `warning` → medium; `info` → low), normalize it. Security findings rated high are fixed first.

## Step 5 — Apply fixes

Apply high and medium fixes directly — the user does not fix code manually. For each fix: apply, run the test command, run the lint command. If tests break: revert, diagnose, try another approach, up to 3 attempts. After 3 failures, append an entry to `.vibe/escalations.md` (append-only; `## [YYYY-MM-DD] /vibe:review — [short title]` then `**Context:**`, `**Attempts:**`, `**Diagnosis:**`, `**Status:** open`, one short sentence each), skip that fix, and report the diagnosis.

Low findings are reported, never auto-fixed.

## Step 6 — Sync, record, commit

1. If fixes were applied: invoke the `vibe:sync` skill.
2. Write `.vibe/last-review.md` (read by feature/fix/backlog for the review cadence hint):

```markdown
# Last review
date: YYYY-MM-DD
commit: [current HEAD hash]
```

3. Commit on every run: `refactor: apply code quality fixes from vibe:review` if fixes were applied, otherwise `chore: record vibe:review run`. Include `CLAUDE.md` if Step 1 flipped a row.

## Step 7 — Report

Short, plain sentences; synthesize, never dump raw agent output:
- Agents run, and any table row flipped in Step 1 (agent, old → new, why)
- Findings: total and per severity
- Applied fixes: file + one line each (or "None")
- Remaining findings by severity, with the diagnosis for each failed fix
- Test status after fixes
