---
type: llm
focus: last_message
criteria: |
  `render_pdf` in fixtures/shipping/labels.py runs `subprocess.run(
  ["wkhtmltopdf", ...])` synchronously. Its only caller, `print_label` in
  fixtures/api/app.py (outside the scope), runs it through
  `asyncio.to_thread(...)`, so the event loop keeps serving other requests
  while a label renders.

  PASS if no `high` or `medium` severity `Blocking` (or clearly equivalent
  category name) finding targets `render_pdf` or its subprocess call. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if the subprocess call is reported as blocking the event loop (or a
  request path) at high or medium severity.
weight: 2
---

Does not call a synchronous function Blocking when its only caller,
outside the scope, already runs it off the event loop.
