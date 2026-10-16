---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "Initial release of reportkit with CSV export and basic pagination\\s*$"
weight: 1
---

The released `[1.0.0]` section is the last thing in the file and must stay
so: new entries go under `[Unreleased]`, never appended below the last
version.
