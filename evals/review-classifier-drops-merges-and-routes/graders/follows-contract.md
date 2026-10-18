---
type: regex
target: last_message
pattern: "## CLASSIFIED findings[\\s\\S]*## DISCARDED[\\s\\S]*## DOUBTS"
weight: 1
---

The three sections of the output contract are present, in order. The
orchestrator parses them by heading.
