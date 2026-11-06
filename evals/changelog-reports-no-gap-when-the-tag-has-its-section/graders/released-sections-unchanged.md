---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[1\\.1\\.0\\] - 2026-08-12\\n\\n### Added\\n\\n- Export a monthly report as CSV\\n\\n## \\[1\\.0\\.0\\] - 2026-06-01\\n\\n### Added\\n\\n- Paginate the report list\\s*$"
weight: 1
---

Both released sections stay byte-for-byte untouched and remain the end
of the file.
