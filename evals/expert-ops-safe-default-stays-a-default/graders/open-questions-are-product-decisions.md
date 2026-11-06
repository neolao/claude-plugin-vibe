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
  wants, for example whether a day's export that could not complete may
  reach the accounting tool a day late, or who is told when it does not),
  each answerable by someone who does not read code.
  FAIL if it asks the caller to settle a technical detail the expert could
  decide itself (whether the defaults should be required, the timeout or
  batch values, the valid range, whether to log the effective values, the
  retry policy), or phrases a question in terms a non-technical Product
  Owner could not answer.
weight: 1
---

Keeps `OPEN QUESTIONS:` for real product decisions, phrased for a
non-technical Product Owner — or omits the list entirely.
