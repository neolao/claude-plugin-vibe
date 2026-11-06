---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[1\\.2\\.0\\] - 2026-09-01\\n\\n### Added\\n\\n- Export a monthly report as CSV\\s*$"
weight: 1
---

The released `[1.2.0]` section stays byte-for-byte untouched and remains
the end of the file.
