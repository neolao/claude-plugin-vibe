---
type: regex
target: { source: file, path: README.md }
pattern: "Widgetcli started as a personal weekend project to learn how to package small CLI tools; this paragraph is maintained entirely by hand and must never be rewritten by any tooling, no matter what else changes in this file\\."
match: contains
weight: 2
---

The hand-written README paragraph outside the managed markers survives
byte-for-byte, whatever source the features came from.
