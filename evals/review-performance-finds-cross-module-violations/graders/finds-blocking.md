---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Blocking` (or clearly equivalent
  category name) finding for the synchronous `subprocess.run(["wkhtmltopdf",
  ...])` in `render_pdf` (fixtures/shipping/labels.py), reached from the
  `async def print_label` handler in fixtures/shipping/app.py, which stalls
  the service's single event loop for every other request while the PDF
  renders (up to the 30s timeout). The fix direction should move it off the
  loop (an async subprocess, an executor, or a worker).
  FAIL if no finding flags this synchronous subprocess call on the event loop.
weight: 1
---

Reports the synchronous wkhtmltopdf call behind the async `print_label`
handler as `Blocking`. labels.py alone is an ordinary sync function; only
app.py shows it runs on the event loop.
