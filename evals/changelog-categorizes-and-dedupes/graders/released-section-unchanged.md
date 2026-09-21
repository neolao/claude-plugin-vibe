---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[1\\.0\\.0\\] - 2026-06-01\\n\\n### Added\\n\\n- Initial release of reportkit with CSV export and basic pagination"
weight: 2
---

The already-released `[1.0.0]` section must stay byte-for-byte untouched —
this skill only ever fills `[Unreleased]`; cutting a version is
`/vibe:release`'s job.
