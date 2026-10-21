---
name: review
description: Runs the project's active review agents on a scope and returns their raw findings — one owner per dimension, the shared finding contract injected into every prompt — without judging, fixing or committing anything. Invoked by the build workflow (`vibe:feature`, `vibe:fix`) as its internal review step and by `vibe:audit`, never directly by users.
argument-hint: "[mode: internal] <changed files, space-separated — or a path to review, empty for the full codebase>"
user-invocable: false
version: 2.1.1
model: claude-sonnet-5-5
---

# vibe:review — Review Agents Brick

Run the specialized `vibe:review-*` agents declared in `CLAUDE.md` on a scope and hand their findings back to the caller. Each agent covers one dimension; the shared finding contract below is what makes their output mergeable. Deciding which findings hold, their level and their space is `vibe:findings-classifier`'s job; fixing is the caller's. This skill edits no code and commits nothing.

## Step 1 — Determine the active agents

Read the `## Review agents` table in `CLAUDE.md`. If it is absent, apply the defaults:

| Agent | Active when |
|---|---|
| `review-tests`, `review-naming`, `review-security`, `review-dependencies`, `review-robustness`, `review-hygiene`, `review-antipatterns`, `review-simplicity`, `review-overengineering`, `review-correctness`, `review-comments`, `review-signatures`, `review-coordination` | always |
| `review-solid` | the codebase has classes or interfaces |
| `review-architecture` | `.vibe/` exists (covers ports & adapters when the project explicitly follows hexagonal architecture) |
| `review-performance` | API/server/full-stack app, or a real-time render/update loop |
| `review-web-security` | the project exposes HTTP endpoints. Its **dynamic verification** mode (probing a locally-run instance) is opt-in: only when the table marks the row `✅ (dynamic)` |
| `review-docs` | Markdown documentation beyond the README exists (`docs/`, `.vibe/`, ADRs, `.claude/rules/`) |
| `review-ddd`, `review-alternative-design` | explicit opt-in only |

An agent absent from an existing table is a new agent: add its row using the condition above, and list it among the flipped rows.

If the table exists, re-check every row against the project as it is now, using the same conditions:
- The reason column decides. A deliberate user choice ("by deliberate choice", "explicit opt-out", `(dynamic)`) is never overridden.
- A reason stating a project fact that is no longer true (no HTTP surface while routes exist, no `.vibe/` while it exists, no tests while a suite appeared — or the reverse) → flip the row and rewrite the reason, in the working tree. Every flipped row is listed in the output; the caller commits `CLAUDE.md` with its own commit.

## Step 2 — Scope

A first line `mode: internal` in `$ARGUMENTS` (the same convention as `clarify` and `rewrite`) means the lines that follow list the changed files to review: the agents read anything they need but report only on those files. Without it, `$ARGUMENTS` is a path; empty means the full codebase. Do not enumerate files yourself beyond the list given — each agent scans on its own. Exclusions passed to every agent: `node_modules/`, `vendor/`, `.venv/`, `dist/`, `build/`, `out/`, `target/`, generated files, `*.config.*`, `*.json` without logic (dependency manifests and lockfiles always stay in scope), migration files.

## Step 3 — Run the active agents in parallel

Launch every active agent in one message (Agent tool, `subagent_type: "vibe:review-<dimension>"`). These launches are part of the workflow the user started (`/vibe:feature`, `/vibe:fix`); a session rule limiting sub-agents does not apply to them. If launching agents is genuinely impossible, say so and stop rather than return a partial review.

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

## Step 4 — Return the findings

Return, and nothing else:

```
## REVIEW agents
- <agent>: <n> finding(s)   — one line per agent run, `0` included
## REVIEW flipped rows
- <agent>: <old> → <new> — <reason>   — or `none`
## REVIEW findings
<every finding, verbatim, in the contract format, each preceded by `AGENT: <agent>`>
```

No merge, no severity change, no fix, no summary: an agent's `SEVERITY` is its suggestion, the classifier decides. An agent that returned nothing contributes its `0` line and no finding.
