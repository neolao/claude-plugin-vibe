---
type: regex
target: trace
pattern: "(?=[\\s\\S]*usage-report\\.sh [^ ]* brick clarify)(?=[\\s\\S]*usage-report\\.sh [^ ]* brick review)(?=[\\s\\S]*usage-report\\.sh [^ ]* brick findings-classifier)"
weight: 1
---

The three bricks reach the counters through the script, spelled as the agents and skills are named, without the `vibe:` prefix.
