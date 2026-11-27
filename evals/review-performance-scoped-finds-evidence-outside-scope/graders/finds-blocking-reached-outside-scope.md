---
type: llm
focus: last_message
criteria: |
  `render_pdf` in fixtures/shipping/labels.py runs `subprocess.run(
  ["wkhtmltopdf", ...])` synchronously (up to its 30 s timeout);
  `print_label` in fixtures/api/app.py, outside the scope, is an `async def`
  handler that calls it directly, so the service's single event loop stalls
  for every other request while a label renders.

  PASS if the reported findings include a `Blocking` (or clearly equivalent
  category name) finding whose FILE: line points to
  fixtures/shipping/labels.py, that names the synchronous subprocess call,
  and whose ISSUE or SUGGESTION names `print_label`, fixtures/api/app.py or
  the event loop it runs on as what makes the call blocking. The fix
  direction should move the call off the loop (an async subprocess, a
  thread or an executor, a worker).
  FAIL if no finding reports this synchronous subprocess call, or if the
  finding is anchored (its FILE: line) on fixtures/api/app.py.
weight: 2
---

Reports the synchronous function in scope as Blocking once its outside
caller shows it runs on the event loop: labels.py alone is an ordinary
sync function.
