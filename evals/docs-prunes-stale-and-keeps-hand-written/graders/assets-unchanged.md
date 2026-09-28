---
type: regex
target: { source: file, path: docs/logo.svg }
pattern: "<rect id=\"widgetcli-logo-mark\" x=\"8\" y=\"8\" width=\"48\" height=\"48\" rx=\"10\" fill=\"#3b6\"/></svg>"
match: contains
weight: 1
---

Non-Markdown files in `docs/` are never modified.
