---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  specific brief, that running unmodified on both Linux build servers and
  macOS developer laptops means avoiding GNU-only coreutils behavior (e.g.
  `sed -i`, `date`, `stat` flag differences) or using portable/POSIX-safe
  equivalents.
  FAIL if the reply never raises GNU-vs-BSD/macOS coreutils portability for
  this brief's dual-OS requirement.
weight: 2
---

Names GNU-vs-BSD/macOS coreutils portability tailored to the Linux-server +
macOS-laptop requirement.
