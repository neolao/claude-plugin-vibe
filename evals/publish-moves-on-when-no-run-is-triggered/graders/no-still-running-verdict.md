---
type: regex
target: last_message
pattern: "still running after"
match: not_contains
flags: i
weight: 2
---

With no run to poll, the ten-minute "still running" verdict cannot apply:
its presence means the step polled an absent run until its total bound.
