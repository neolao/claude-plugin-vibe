---
name: review-dependencies-no-false-positives
description: review-dependencies must not flag express's exact pin, lodash/date-fns's caret ranges backed by a committed lockfile, or jest's correctly-scoped devDependency use
tags: [review-dependencies, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-dependencies` sub-agent (Agent tool, `subagent_type: "vibe:review-dependencies"`) to review `fixtures/` in this case directory. Give it exactly this prompt:

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

Once the sub-agent returns, report its findings back verbatim (or state that it found nothing).
