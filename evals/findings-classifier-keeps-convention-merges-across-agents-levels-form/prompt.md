---
name: findings-classifier-keeps-convention-merges-across-agents-levels-form
description: >-
  findings-classifier must drop a finding that the project's written convention blesses, merge a bug and its missing-test finding raised by two agents on the same line, and give a naming finding the low level whatever severity its agent suggested
tags: [findings-classifier, hardening]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:findings-classifier` sub-agent (Agent tool, `subagent_type: "vibe:findings-classifier"`) with exactly this prompt:

```
Classify the findings below. Working directory: the current directory; the deliverable is the code in `fixtures/`. Type of deliverable: code.

REQUEST (brief approved by the Product Owner):
"GET /notes?page=N returns the Nth page of 20 notes, pages starting at 1."

RAW FINDINGS:
1. review-robustness — fixtures/handlers.py:16 — `get_notes` catches `Exception` and returns the error text in a 500 response; errors are swallowed in a broad handler.
2. review-correctness — fixtures/handlers.py:14 — `start = page * PAGE_SIZE` skips the first 20 notes: `page=1` returns the second page.
3. review-tests — fixtures/handlers.py:14 — no test requests `page=1`, so the first page is never checked to be returned.
4. review-naming — fixtures/handlers.py:16 — the variable `exc` could be named `error`. Suggested severity: high.
```

Once the sub-agent returns, report its output back verbatim.
