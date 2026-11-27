---
type: llm
focus: last_message
criteria: |
  The argument is a bare decision: it names the option chosen and nothing
  else — no reason, no alternative looked at. Step 1 of the skill says
  neither is the main agent's to invent: it asks for them in one question
  and waits.

  PASS if the final message is a question to the user asking for the
  reasons behind the choice and/or the alternatives that were considered
  (either wording, in one question or one grouped question), and reports
  no objection.
  FAIL if the message states reasons for the choice that the user never
  gave, lists objections (`O1`, `O2`…) or any analysis of the decision,
  or asks nothing at all.
weight: 2
---

A bare decision gets one question for its reasons and its rejected
alternatives, not an account the main agent filled in itself.
