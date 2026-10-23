---
type: llm
focus: last_message
criteria: |
  The final message includes the raw output of `git tag -n20 v1.2.4`,
  which prints the tag's message.

  PASS if that output shows, below the `v1.2.4` subject, the changelog
  entry "Fix crash when loading a config file with no entries" (its
  `### Fixed` heading may or may not be there).
  FAIL if the output shows only the subject, shows no message at all, or
  is missing from the final message.
weight: 2
---

The tag message carries the version's entries, so the forge and
`git show v1.2.4` say what shipped.
