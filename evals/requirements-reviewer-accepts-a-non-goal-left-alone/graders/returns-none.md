---
type: regex
target: last_message
pattern: "## REQUIREMENTS findings\\s*\\n\\s*none\\s*$"
flags: m
weight: 2
---

With nothing to report, the output is exactly the heading and `none`: no
recap of the criteria checked, no list of dismissed points.
