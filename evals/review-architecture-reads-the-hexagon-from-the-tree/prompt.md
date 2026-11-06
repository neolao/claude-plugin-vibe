---
name: review-architecture-reads-the-hexagon-from-the-tree
description: >-
  review-architecture must read the hexagon from the tree alone — no ADR,
  no CLAUDE.md, no decisions directory, but fixtures/core/ports/ and
  fixtures/adapters/ exist — and report `NotifierPort`, defined in
  fixtures/adapters/smtp_notifier.py and imported by
  fixtures/core/order_service.py, as a port on the adapter side, while
  giving no port finding to the `PricingPolicy` protocol implemented by two
  core classes in fixtures/core/pricing/policy.py
tags: [review-architecture, recall, hexagonal]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-architecture` sub-agent (Agent tool, `subagent_type: "vibe:review-architecture"`) to review `fixtures/` in this case directory. `.vibe/` is present at the workspace root, as it is when the internal review runs for real. Give it exactly this prompt:

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

Scope: fixtures/
Exclusions: node_modules/, vendor/, .venv/, dist/, build/, out/, target/, generated files, *.config.*, *.json without logic (dependency manifests and lockfiles always stay in scope), migration files.
```

Once the sub-agent returns, report its findings back verbatim.
