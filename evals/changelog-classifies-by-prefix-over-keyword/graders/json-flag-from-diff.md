---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*json"
flags: i
weight: 2
---

`Monday changes` matches no prefix and no keyword; its diff adds a
`--json` flag to the report command. The entry comes from the diff, under
whichever category the skill judges right (Added or Changed), and names
the JSON output.
