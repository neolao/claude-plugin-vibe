---
type: llm
focus: last_message
criteria: |
  Item 002 has `status: blocked` and a `## Blocked` section reading
  "the till export has no stable column order, so no parser can be pinned yet".

  PASS if the report reproduces or paraphrases that reason for 002 — the
  unstable column order of the till export.
  FAIL if 002 is only shown as blocked with no reason, or the reason given is
  not the one in the file.
weight: 2
---

Surfaces 002's own `## Blocked` reason, not just its status.
