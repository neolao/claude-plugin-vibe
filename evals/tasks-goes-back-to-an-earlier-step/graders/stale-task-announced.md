---
type: regex
target: last_message
pattern: "✗\\s*Commit\\s*[—-]+\\s*stale"
weight: 1
---

The only `pending` task at the time of the return ("Commit") was dropped
and announced with the skill's exact line `✗ <subject> — stale`, not with
free prose.
