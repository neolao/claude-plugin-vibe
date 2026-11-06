---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## 1\\.0\\.0 - 2026-06-01\\n\\n### Added\\n\\n- Paginate the report list\\s*$"
weight: 1
---

The released `1.0.0` section stays byte-for-byte untouched — its
bracketless heading included — and remains the end of the file.
