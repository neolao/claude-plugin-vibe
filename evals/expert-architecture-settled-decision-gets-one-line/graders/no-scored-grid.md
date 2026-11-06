---
type: llm
focus: last_message
criteria: |
  The expert's own rule: when the repo already prescribes the form, the
  reply is one line saying so and naming the decision or the idiom,
  "whatever format the request asks for — never lists filled with generic
  advice". The request here asks for BASELINE / ALTERNATIVES /
  RECOMMENDATION; the decision makes that grid pointless.

  PASS if the reply is a short statement (one line, or a few lines at most)
  with no alternative scored against a baseline, no BETTER / TIE / WORSE
  verdict, and no structure other than the registered adapter module — a
  sentence saying what the SMS module is (one module under
  `adapters/notify/`, registered as "sms", imported in `__init__.py`)
  passes.
  FAIL if the reply fills BASELINE and ALTERNATIVES with options and
  verdicts, scores a named pattern against the registry, or recommends a
  structure the decision rejected (a channel base class with subclasses, a
  branch or match on the channel name in the router).
weight: 2
---

Replies in one line instead of scoring options for a choice the decision
already closed.
