---
type: regex
target: { source: file, path: docs/contributing.md }
pattern: "^# Contributing\n\nWe review pull requests on Tuesdays and Thursdays; ping the maintainers channel if yours has waited longer than a week\\.\n\nRun `npm test` before opening a pull request\\.\n?$"
weight: 2
---

`docs/contributing.md` has no banner, so it is hand-written: the skill must
leave it exactly as it was, without adding a banner or rewording it.
