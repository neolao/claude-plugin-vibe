---
type: llm
focus: last_message
criteria: |
  The last commit predates the `2024-02-01` date in `.vibe/index.md` and the
  working tree is clean, so Step 1 finds no changed source file.

  PASS if the report says `.vibe/` was already up to date and nothing needed
  updating.
  FAIL if it claims to have updated, regenerated, or refreshed anything.
weight: 2
---

Reports "already up to date" instead of doing work.
