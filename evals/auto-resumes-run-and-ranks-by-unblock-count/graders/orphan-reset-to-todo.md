---
type: regex
pattern: 'status:\s*todo'
target: { source: file, path: ".vibe/backlog/006-add-mode-helper.md" }
match: contains
weight: 2
---

Item 006 was left `status: in_progress` by an earlier crash and is not this
run's `current`. Step 0's last rule puts such an orphan back to `status: todo`.
