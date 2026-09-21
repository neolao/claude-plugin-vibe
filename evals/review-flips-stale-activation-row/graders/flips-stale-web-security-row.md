---
type: regex
target: { source: file, path: "CLAUDE.md" }
pattern: "review-web-security[^|]*\\|\\s*✅"
weight: 2
---

`review-web-security`'s row claimed "no HTTP surface in this project" while
`app.py` declares two Flask routes. Step 1 says a reason stating a project
fact that is no longer true must flip the row — so the table must now mark
this agent active.
