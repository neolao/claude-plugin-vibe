---
type: llm
focus: last_message
criteria: |
  `fanout` in fixtures/app.py starts one `threading.Thread` per entry of
  the `contacts` list the client posts, with no pool, queue or bound on
  the list's length: one request starts as many threads as its body
  lists, and a flood of them exhausts the process.

  PASS if the reported findings include a `DoS` (or clearly equivalent
  category name) finding on `fanout`, for the thread per client-chosen
  contact with no bound.
  FAIL if no finding reports `fanout`'s unbounded thread creation.
weight: 2
---

Reports workers only an attacker's request count fills as DoS.
