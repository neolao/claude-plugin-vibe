---
name: review
description: Run code quality review using specialized sub-agents defined in CLAUDE.md
argument-hint: "[optional: path or file to review — defaults to full codebase]"
---

# /vibe:review — Code Quality Review Orchestrator

Run a structured code quality review by invoking the specialized agents declared in `CLAUDE.md`. Each agent focuses on one dimension only.

## Step 1 — Read configuration

Read `CLAUDE.md` and find the `## Review agents` section.
It lists which agents are active for this project and their scope.

If the section is absent, apply these defaults:
- **Always active:** `vibe:review-tests`, `vibe:review-naming`, `vibe:review-complexity`, `vibe:review-security`, `vibe:review-dependencies`, `vibe:review-robustness`, `vibe:review-hygiene`, `vibe:review-antipatterns`, `vibe:review-simplicity`, `vibe:review-overengineering`
- **Conditional:** `vibe:review-solid` if the codebase contains classes or interfaces; `vibe:review-architecture` if `.vibe/` exists; `vibe:review-performance` if the project is an API/server/full-stack app; `vibe:review-web-security` if the project exposes HTTP endpoints; `vibe:review-pentest` if the project exposes a runnable networked application that can be exercised in a safe local environment; `vibe:review-hexagonal` if the project explicitly follows a hexagonal (ports & adapters) architecture — declared in an ADR or `CLAUDE.md`, or evident from a `ports/`/`adapters/` structure
- **Skip:** `vibe:review-ddd` (explicit opt-in required)

### Step 1a — Re-check the table against the current project state

If the section exists, do not trust it blindly — the project may have changed since `/vibe:init` wrote it. For each row, re-evaluate the agent's activation condition (the same rules as the defaults above) against the project as it is now, then reconcile:

- **The reason column is what decides.** If it records a deliberate user choice (e.g. "by deliberate choice", "explicit opt-out"), respect the row as-is — never override it.
- If it states a project fact that is **no longer true** — "no HTTP surface" while routes now exist, "run /vibe:sync first" while `.vibe/` now exists, "no test suite" while one has appeared — update the row in `CLAUDE.md`: flip the status and rewrite the reason to match reality. The same applies in both directions (an agent may also become inactive, e.g. an HTTP surface that was removed).
- Every row changed this way MUST be listed in the final report (Step 7), so the user can spot and revert a wrong flip. The updated `CLAUDE.md` is committed with the rest of the run in Step 6.

Use the reconciled table to determine the active agents for this run.

## Step 1b — Create task list

Based on the active agents determined in Step 1, create tasks using TaskCreate. Always include the three mandatory agents. Add optional agents only if active. The `Run review-*` tasks are independent (no `blockedBy` between them) — they run in parallel. **Keep subject names short (≤ 30 chars)** — they appear in the status line.

```
Run vibe:review-tests              ← no dependency
Run vibe:review-naming             ← no dependency
Run vibe:review-complexity         ← no dependency
Run vibe:review-security           ← no dependency
Run vibe:review-dependencies       ← no dependency
Run vibe:review-robustness         ← no dependency
Run vibe:review-hygiene            ← no dependency
Run vibe:review-antipatterns       ← no dependency
Run vibe:review-simplicity         ← no dependency
Run vibe:review-overengineering    ← no dependency
[Run vibe:review-solid]            ← no dependency (if active)
[Run vibe:review-ddd]              ← no dependency (if active)
[Run vibe:review-architecture]     ← no dependency (if active)
[Run vibe:review-performance]      ← no dependency (if active)
[Run vibe:review-web-security]     ← no dependency (if active)
[Run vibe:review-pentest]          ← no dependency (if active)
[Run vibe:review-hexagonal]        ← no dependency (if active)
Deduplicate and prioritize    ← blockedBy ALL "Run review-*" tasks
Apply fixes                   ← blockedBy "Deduplicate and prioritize"
Sync .vibe/ and commit        ← blockedBy "Apply fixes"
```

## Step 2 — Determine scope

- If `$ARGUMENTS` is provided: the scope is the specified path or file.
- If no argument: the scope is the full codebase.

Do not enumerate files yourself — each agent scans the code on its own. Instead, pass the scope to every agent in Step 3, along with this exclusion list: `node_modules/`, `vendor/`, `.venv/`, `dist/`, `build/`, `out/`, `target/`, generated files (`// generated`, `# auto-generated`), `*.config.*`, `*.json` (unless it contains logic), migration files.

## Step 3 — Run active agents in parallel

Mark ALL `Run review-*` tasks `in_progress`, then launch every active agent **in parallel** — a single message containing one Agent call per active agent (`subagent_type: "vibe:review-<dimension>"`). Include the scope and exclusion list from Step 2 in each agent's prompt. They are all read-only, so there is no conflict; running them sequentially only wastes time.

Once launched, simply wait: each agent's completion arrives automatically as a notification when it finishes — there is nothing else to do to "wait" for them. Do not schedule a wakeup or poll for their status; that machinery is for external state the harness cannot track (a CI run, a remote queue), not for agents launched via the Agent tool, which already notify on completion.

- `Run vibe:review-tests` — test relevance, quality, and real execution: invoke the `vibe:review-tests` agent via the Agent tool (`subagent_type: "vibe:review-tests"`). Unlike the other dimension agents, it actually executes the project's test suite (including isolated e2e/integration runs) to ground findings in real pass/fail evidence, not just static reading. Core principle: **tests must verify observable behaviour, not implementation details** — a test that breaks on refactoring without any behaviour change is a false test. Collect all findings (coverage gaps, relevance issues, quality issues).
- `Run vibe:review-naming` — naming issues
- `Run vibe:review-complexity` — complexity hotspots
- `Run vibe:review-security` — code-level security: committed secrets, injections, dangerous primitives, missing access control, crypto misuse
- `Run vibe:review-dependencies` — dependency health: runs the stack's audit tool (CVEs), abandoned packages, version hygiene, unused deps
- `Run vibe:review-robustness` — failure behavior: swallowed errors, unawaited promises, missing timeouts, unclosed resources
- `Run vibe:review-hygiene` — dead code, leftovers, stale TODOs, copy-paste duplication
- `Run vibe:review-antipatterns` — named anti-patterns: god objects, primitive obsession, stringly-typed code, mutable global state, temporal coupling, wheel reinvention
- `Run vibe:review-simplicity` — expression-level convolution: redundant conditions, pointless indirection, non-idiomatic detours, reducible logic
- `Run vibe:review-overengineering` — design-level YAGNI: speculative abstractions, unused configurability, premature optimization, disproportionate layering
- `Run vibe:review-solid` — SOLID violations (if active)
- `Run vibe:review-ddd` — DDD alignment (if active)
- `Run vibe:review-architecture` — architectural drift: module boundaries, circular deps, layer violations, violations of recorded decisions — ADRs in `.vibe/decisions/` (or legacy `.vibe/decisions.md`) (if active — requires `.vibe/`)
- `Run vibe:review-performance` — clear performance defects: N+1, quadratic patterns, blocking I/O on hot paths, unbounded caches (if active)
- `Run vibe:review-web-security` — deep web audit: path traversal, XSS, SSRF, security headers, cookies, application-level DoS (if active)
- `Run vibe:review-pentest` — dynamic penetration test against a locally-run instance: proves auth bypass, IDOR, injection, business-logic abuse, and exploit chains against the live app (if active — authorized local scope only)
- `Run vibe:review-hexagonal` — ports & adapters compliance: port ownership, leaky port contracts, adapter purity, wiring (if active — hexagonal projects only)

As each agent returns, collect its findings and mark its task `completed`.

## Step 4 — Deduplicate and prioritize

Mark the `Deduplicate and prioritize` task `in_progress`.

- Merge findings that point to the same issue from different angles
- Normalize severities — the agents use different scales:

| Agent scale | Normalized priority |
|---|---|
| `critical`, `high`, `problem` | **High** |
| `medium`, `warning` | **Medium** |
| `low`, `info` | **Low** |

- Priority meaning:
  - **High** — affects correctness, security, or maintainability significantly
  - **Medium** — reduces readability or violates a clear principle
  - **Low** — style preference or minor improvement
- Security findings normalized to High are handled FIRST in Step 5.

Mark the task `completed`.

## Step 5 — Apply fixes

Mark the `Apply fixes` task `in_progress`.

Apply High and Medium priority fixes directly — this is vibe coding: the user does not fix code manually.

For each fix:
1. Apply it
2. Run the test command (from manifest) to confirm nothing broke
3. Run the lint command (from manifest)
4. If tests break: revert, diagnose, try an alternative approach — repeat up to 3 times
5. If still failing after 3 attempts: append an entry to the escalation log `.vibe/escalations.md` (create the file if absent; append-only — heading `## [YYYY-MM-DD] /vibe:review — [short title]` followed by `**Context:**`, `**Attempts:**`, `**Diagnosis:**`, `**Status:** open` lines — same shape as `skills/feature/SKILL.md` and `skills/fix/SKILL.md`, canonical form in `.vibe/models.md` ("Escalation entry"); update all three together), then skip that fix and escalate to the user with a precise diagnosis

Do NOT auto-fix Low findings — report them only.

Mark the task `completed`.

## Step 6 — Sync .vibe/, record the run, and commit

Mark the `Sync .vibe/ and commit` task `in_progress`.

1. If any fixes were applied in Step 5: **invoke the `vibe:sync` skill** using the Skill tool (`skill: "vibe:sync"`) — to update affected module documentation.
2. Write (or overwrite) the review cadence marker `.vibe/last-review.md` — it is read by `/vibe:feature`, `/vibe:fix`, and `/vibe:backlog` to suggest the next review:

```markdown
# Last review
date: YYYY-MM-DD
commit: [current HEAD hash]
```

3. Commit — this happens on **every** run, fixes or not:
   - If fixes were applied: stage all modified files (including the marker and, if Step 1a updated the agent table, `CLAUDE.md`) and commit `refactor: apply code quality fixes from vibe:review`
   - If no fix was applied: commit the marker (plus `CLAUDE.md` if Step 1a updated the agent table) — `chore: record vibe:review run`

Mark the task `completed`.

## Step 7 — Report to user

Structure the report as follows:

```
## Review summary

Agents run: [list]
Agent table updated: [each row flipped by Step 1a — agent, old → new status, why; omit this line if none]
Files reviewed: N
Total findings: N (High: N, Medium: N, Low: N)

## Applied fixes (High + Medium)
[list of what was changed, with file + one-line description]
[or "None" if nothing was auto-fixed]

## Remaining findings

### High
[list — auto-fix failed after 3 attempts; includes diagnosis]

### Medium
[list — auto-fix failed after 3 attempts; includes diagnosis]

### Low
[list — address when convenient]

## Test status after fixes
[result of test run]
```

Keep the report scannable. Do not dump raw agent output — synthesize it.
