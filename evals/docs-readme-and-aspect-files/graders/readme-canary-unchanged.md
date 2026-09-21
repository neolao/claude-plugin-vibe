---
type: regex
target: { source: file, path: README.md }
pattern: "Widgetcli started as a personal weekend project to learn how to package small CLI tools; this paragraph is maintained entirely by hand and must never be rewritten by any tooling, no matter what else changes in this file\\."
match: contains
weight: 3
---

Precision check — the most important grader in this case. The hand-written
paragraph outside the managed markers must survive byte-for-byte: the skill
must never touch non-managed README content, no matter what else it rewrites
around it.
