---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Module scope` (or clearly
  equivalent category name) finding on `fixtures/core/email_templates.py`
  (or on the `core` module because of it), for a file that renders HTML and
  sends mail over SMTP inside a zone whose `.vibe/modules/core.md` role is
  "pure business/domain logic ... no I/O, no framework, database, or mail
  imports", and which that module's `Files:` list does not even mention.
  FAIL if no finding flags this file as outside the declared scope of the
  `core` module.
weight: 1
---

Reports the HTML-rendering, SMTP-sending file sitting inside `core/` as a
`Module scope` finding against the module's declared role and file list.
