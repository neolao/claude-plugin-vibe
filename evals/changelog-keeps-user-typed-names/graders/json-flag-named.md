---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*### Added(?:(?!\\n##)[\\s\\S])*--json"
weight: 3
---

`--json` is what the user types to get the new output: the `### Added`
entry under `[Unreleased]` must name it. Dropping it in the name of
"no identifiers" would leave the user with an entry they cannot act on.
