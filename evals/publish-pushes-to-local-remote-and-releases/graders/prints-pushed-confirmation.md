---
type: regex
target: last_message
pattern: "✓\\s*pushed"
weight: 1
---

`vibe:publish` prints `✓ pushed` on a successful Step 1 push. The starting
tree has local commits ahead of `origin`, so this must succeed.
