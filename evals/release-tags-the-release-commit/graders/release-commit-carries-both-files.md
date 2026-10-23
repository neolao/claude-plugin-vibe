---
type: llm
focus: last_message
criteria: |
  The final message includes the raw output of `git show --stat --format='%s' HEAD`.

  PASS if that output names `chore: release v1.2.4` as the subject and
  lists both `CHANGELOG.md` and `package.json` among the changed files.
  FAIL if either file is missing from the commit, the subject differs,
  or the output is absent.
weight: 2
---

The release commit carries the cut and the bump together.
