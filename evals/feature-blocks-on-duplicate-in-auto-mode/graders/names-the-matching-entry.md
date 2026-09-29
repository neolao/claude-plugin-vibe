---
type: llm
focus: last_message
criteria: |
  PASS if the final report identifies the existing capability that makes the
  brief a duplicate: it points at the `[Unreleased]` changelog entry about
  getting the middle value of a list (or at the existing `middleValue`
  function) and says that this is what the brief asks for.
  FAIL if it reports a duplicate without saying what it duplicates, or names
  something unrelated.
weight: 2
---

The verdict alone is not enough for a human to act on: the report must say
what the brief collides with.
