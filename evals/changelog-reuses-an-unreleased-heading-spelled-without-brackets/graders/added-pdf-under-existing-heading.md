---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## Unreleased\\n(?:(?!\\n## )[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*PDF"
weight: 2
---

The PDF export lands under `### Added` inside the existing `## Unreleased`
heading, spelled as it was.
