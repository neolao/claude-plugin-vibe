---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[1\\.3\\.0-rc\\.1\\] - 2026-10-20\\n\\n### Added\\n\\n- Export a monthly report as CSV\\n\\n## \\[1\\.2\\.0\\] - 2026-09-01\\n\\n### Added\\n\\n- Paginate the report list\\s*$"
weight: 1
---

Both released sections, `[1.3.0-rc.1]` and `[1.2.0]`, stay byte-for-byte
untouched and remain the end of the file.
