---
name: review-architecture-finds-violations
description: review-architecture must find module scope drift, a circular dependency, wrong layer direction, responsibility spread, a violated decision, an orphaned module, and port/adapter violations (port ownership, leaky port, adapter purity, wiring) against the `.vibe/` module map
tags: [review-architecture, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-architecture` sub-agent (Agent tool, `subagent_type: "vibe:review-architecture"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when `/vibe:review` runs for real. Give it exactly this prompt:

```
Review the code in scope for your dimension only. Read-only: never edit, create, or run anything the agent definition does not explicitly allow.
Report every finding as:

FILE: path/to/file (line N)
CATEGORY: <one of your categories>
SEVERITY: high | medium | low
ISSUE: what is wrong and why it matters — one or two sentences
SUGGESTION: concrete fix direction — one or two sentences

Severity: high = correctness, security, or a bug that will ship; medium = a clear principle or convention broken; low = minor improvement.
Flag only what you can point to in the code, with a plausible failure or cost — no theoretical findings, no metric-chasing. Skip a category with nothing to report. Do not summarize or count at the end.

Scope: fixtures/
```

Once the sub-agent returns, report its findings back verbatim.
