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
  wants, for example how long after payment a shipment may be created during
  a sale, or who is told when the partner rejects an order), each answerable
  by someone who does not read code.
  FAIL if it asks the caller to settle a technical detail the expert could
  decide itself (whether to forbid overlapping runs or how, a lock or a
  concurrency policy, a timeout value, the run interval, a batch size, which
  alerting channel or metric, how to make the partner call idempotent), or
  phrases a question in terms a non-technical Product Owner could not answer.
weight: 1
---

Keeps `OPEN QUESTIONS:` for real product decisions, phrased for a
non-technical Product Owner — or omits the list entirely.
