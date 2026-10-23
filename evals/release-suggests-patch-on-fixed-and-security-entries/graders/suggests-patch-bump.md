---
type: llm
focus: last_message
criteria: |
  PASS if the final report states the suggested bump was `patch` (or the
  version 1.2.4), with reasoning tied to the `[Unreleased]` section
  holding only Fixed and Security entries — nothing added, nothing
  changed, nothing removed.
  FAIL if the bump is reported as minor or major, or if patch is stated
  with no reasoning connecting it to the Fixed and Security entries.
weight: 2
---

Confirms the skill's precedence rule (Security counts with Fixed, as
patch) was followed and explained, not guessed.
