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
  wants, for example how long archived files are kept or who is told when a
  partner file is rejected), each answerable by someone who does not read
  code.
  FAIL if it asks the caller to settle a technical detail the expert could
  decide itself (whether to take a lock, which lock mechanism, which `PATH`,
  a timeout value, where to log, how to make ssh or psql non-interactive),
  or phrases a question in terms a non-technical Product Owner could not
  answer.
weight: 1
---

Keeps `OPEN QUESTIONS:` for real product decisions, phrased for a
non-technical Product Owner — or omits the list entirely.
