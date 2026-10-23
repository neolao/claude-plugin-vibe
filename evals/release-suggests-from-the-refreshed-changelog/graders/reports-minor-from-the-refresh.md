---
type: llm
focus: last_message
criteria: |
  The skill refreshes the changelog from git history before suggesting
  the bump, so the Added entry written from the `feat:` commit is what
  makes the bump minor.

  PASS if the final report states the suggested bump was minor (or the
  version 1.3.0) and ties it to an Added entry / a new feature — the CSV
  export — found when the changelog was brought up to date (saying the
  entry came from a commit, from git history, or from the changelog
  refresh all count).
  FAIL if the bump is reported as patch, if 1.2.4 is named as the
  released version, or if minor is stated with no reason connecting it to
  the Added entry.
weight: 2
---

Confirms the suggestion was made on the complete section and explained,
not read off the stale one and corrected by luck.
