---
type: regex
target: trace
pattern: "(?=[\\s\\S]*incr findings\\.raised 5(?![0-9]))(?=[\\s\\S]*incr findings\\.dropped 1(?![0-9]))(?=[\\s\\S]*incr findings\\.merged 2(?![0-9]))(?=[\\s\\S]*incr findings\\.high 1(?![0-9]))(?=[\\s\\S]*incr findings\\.low 1(?![0-9]))"
weight: 2
---

Every finding quantity of the prompt is counted under its own key: raised 5, dropped 1, merged 2, one high, one low. A kept finding counted under another level is not matched.
