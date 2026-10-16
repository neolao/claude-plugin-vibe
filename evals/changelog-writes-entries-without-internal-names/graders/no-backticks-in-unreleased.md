---
type: regex
target: { source: file, path: CHANGELOG.md }
pattern: "## \\[Unreleased\\](?:(?!\\n## \\[)[\\s\\S])*`"
match: not_contains
weight: 1
---

Nothing in these two commits is a command, flag, endpoint or setting the
user types, so no backticked token has a reason to appear under
`[Unreleased]` — putting an identifier in backticks is still naming it.
