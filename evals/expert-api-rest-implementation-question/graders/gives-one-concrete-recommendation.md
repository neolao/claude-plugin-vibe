---
type: llm
focus: last_message
criteria: |
  PASS if the reply commits to exactly one course of action for the repeated
  call — a specific status code and body behaviour — stated as what to do,
  with the reason it is the right call here.
  FAIL if it presents several options without choosing, or answers "it
  depends" without landing on one.
weight: 2
---

Lands on one concrete recommendation rather than a menu.
