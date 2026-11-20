---
name: review-dependencies-finds-every-manifest
description: On a repository with a Python API (fixtures/api/pyproject.toml, PyYAML==5.3) beside a Node front end (fixtures/web/package.json, lodash 4.17.4), review-dependencies must audit and report on both manifests, with a Vulnerability finding on each pinned version and an audit-could-not-run report that covers both ecosystems
tags: [review-dependencies, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent, Bash]
---

Invoke the `vibe:review-dependencies` sub-agent (Agent tool, `subagent_type: "vibe:review-dependencies"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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
