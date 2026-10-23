---
type: llm
focus: { source: file, path: README.md }
criteria: |
  Look only at the content between `<!-- vibe:begin:features -->` and
  `<!-- vibe:end:features -->` in README.md.

  The project is a bare scaffold: its only source file exports nothing
  and no command exists. The manifest description says it is "a tiny CLI
  to manage widgets", which is the intent, not a capability.

  PASS only if that section presents no capability as available: it says
  there is no feature yet (or nothing usable yet), possibly with one line
  on what the project aims at.

  FAIL if any line presents a capability as if the user could use it
  today — adding, listing, managing or storing widgets, any command, any
  option.
weight: 3
---

The features come from what the code lets the user do. On a scaffold
that is nothing, and the manifest's description is not turned into a
feature list.
