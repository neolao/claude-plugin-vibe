---
type: regex
target: trace
pattern: "(?:usage-report\\.sh [^ ]* incr questions 2(?![0-9])|usage-report\\.sh [^ ]* incr questions(?![ .\\w])[\\s\\S]*usage-report\\.sh [^ ]* incr questions(?![ .\\w]))"
weight: 1
---

The two questions asked by `clarify` are counted, as one `incr questions 2` or as two `incr questions`.
