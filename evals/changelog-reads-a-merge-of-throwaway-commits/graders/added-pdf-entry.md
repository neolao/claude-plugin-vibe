---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
flags: i
weight: 3
---

The branch's three commits say nothing; the merge message does. The PDF
export must land under `### Added` inside `[Unreleased]` — the change is
real even though no single commit describes it.
