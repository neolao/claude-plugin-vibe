---
type: regex
target: trace
pattern: "brick clarify[\\s\\S]*brick review[\\s\\S]*incr findings\\.raised 5[\\s\\S]*brick findings-classifier[\\s\\S]*incr returns\\.implementation[\\s\\S]*incr fixes[\\s\\S]*usage-report\\.sh [^ ]* write "
weight: 1
---

The events are counted in the order they are listed, and `write` comes after the last one: nothing is reconstructed at the end.
