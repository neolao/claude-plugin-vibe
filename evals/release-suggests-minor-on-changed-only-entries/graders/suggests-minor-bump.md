---
type: llm
focus: last_message
criteria: |
  PASS if the final report states the suggested bump was `minor` (or the
  version 1.3.0), with reasoning tied to the `[Unreleased]` section
  holding a `Changed` entry — altered behaviour, not a fix, not a
  breaking change.
  FAIL if the bump is reported as patch or major, or if minor is stated
  with no reasoning connecting it to the Changed entry.
weight: 2
---

Confirms the skill's precedence rule (Changed counts with Added, as minor)
was followed and explained, not guessed.
