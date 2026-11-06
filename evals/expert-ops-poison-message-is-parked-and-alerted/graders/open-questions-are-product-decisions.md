---
type: llm
focus: last_message
criteria: |
  The request allows a fourth list, `OPEN QUESTIONS:` (≤3), "only when a real
  product decision in your domain is genuinely undetermined by the brief — not
  a technical detail you can decide yourself", each phrased for a
  non-technical Product Owner. `/vibe:feature` puts these straight to the user
  in plain words, so a technical question here reaches the wrong person.

  PASS if the reply either has no `OPEN QUESTIONS:` list at all, or lists at
  most 3 questions that are genuine product decisions (what the business
  wants, for example what is done with an order whose update could not be
  applied — who looks at it, whether the partner is told, whether the
  order is blocked meanwhile), each answerable by someone who does not
  read code.
  FAIL if it asks the caller to settle a technical detail the expert could
  decide itself (whether to park failing messages, how many attempts, a
  dead-letter queue versus a table, when to acknowledge, how to
  deduplicate, which alert), or phrases a question in terms a
  non-technical Product Owner could not answer.

  Judge what each question asks, not the reason given after it: a business
  question about what becomes of a parked order passes, because the
  Product Owner can answer it without reading code.
weight: 1
---

Keeps `OPEN QUESTIONS:` for real product decisions, phrased for a
non-technical Product Owner — or omits the list entirely.
