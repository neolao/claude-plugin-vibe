---
type: regex
target: last_message
pattern: "✗\\s*Commit\\s*[—-]+\\s*stale"
weight: 1
---

"Commit" was pending at the time of the return too: it gets its own
`✗ <subject> — stale` line, not one line covering both tasks.
