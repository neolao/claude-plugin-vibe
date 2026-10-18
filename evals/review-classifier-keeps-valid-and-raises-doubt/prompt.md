---
name: review-classifier-keeps-valid-and-raises-doubt
description: review-classifier must keep two valid findings without inventing new ones, drop none of them, and turn the point the request leaves open (which spreadsheet opens the file) into a DOUBT with a recommended option instead of guessing or dismissing
tags: [review-classifier, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:review-classifier` sub-agent (Agent tool, `subagent_type: "vibe:review-classifier"`) with exactly this prompt:

```
Classify the findings below. Working directory: the current directory; the deliverable is the code in `fixtures/`. Type of deliverable: code.

REQUEST (brief approved by the Product Owner):
"Admins can download the monthly report as a CSV file with the date, the amount and the label of each line."

RAW FINDINGS:
1. review-robustness — fixtures/export.py:12 — `row["date"]`, `row["amount"]`, `row["label"]` raise KeyError on a row missing a column; the export aborts on the first incomplete line instead of the admin getting a file.
2. review-correctness — fixtures/export.py:18 — the file is encoded in UTF-8 without a byte-order mark; Excel on Windows opens such a CSV with accented labels garbled, while LibreOffice and Numbers read it fine. The brief does not say which spreadsheet the admins use.
```

Once the sub-agent returns, report its output back verbatim.
