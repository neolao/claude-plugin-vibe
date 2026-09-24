---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[1\\.10\\.0\\] - 2026-08-12\\n\\n### Added\\n\\n- Export a monthly report as CSV\\n\\n## \\[1\\.9\\.0\\] - 2026-07-01\\n\\n### Added\\n\\n- Paginate the report list"
weight: 1
---

Both released sections, `[1.10.0]` and `[1.9.0]`, stay byte-for-byte
untouched: this skill only ever fills `[Unreleased]`.
