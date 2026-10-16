---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[1\\.1\\.0\\] - 2026-07-01\\n\\n### Added\\n\\n- Export a monthly report as PDF\\n\\n## \\[1\\.0\\.0\\] - 2026-06-01\\n\\n### Added\\n\\n- Initial release of reportkit with CSV export and basic pagination"
weight: 2
---

Both released sections stay byte-for-byte untouched — the `[1.1.0]` entry
that announced the PDF export included: history is not rewritten when a
feature is later taken back.
