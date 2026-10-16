---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "# Changelog[\\s\\S]*keepachangelog\\.com"
weight: 1
---

The new file opens with the Keep a Changelog header, not with a bare list.
