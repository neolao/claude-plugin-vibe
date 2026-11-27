---
type: llm
focus: last_message
criteria: |
  fixtures/src/exports/container.py declares a `Container` with
  `register`/`resolve` and a `build_container` that registers one
  factory, `CsvExporter`; its only consumer, fixtures/src/exports/
  run_export.py, resolves that one key. Every other module of the
  project builds its collaborators directly (`InvoiceMailer()` and
  `SqlOrderRepository(db)` in run_billing.py, `InvoiceRenderer()` and
  `smtplib.SMTP(...)` in mailer.py).

  PASS if the reported findings include a `Pattern without need` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/src/exports/container.py (or run_export.py) and that names the
  container, registry or resolve indirection as unneeded where
  `CsvExporter()` could be built directly.
  FAIL if no finding reports the container for this reason.
weight: 2
---

Reports a container brought in for a single dependency in a project
that constructs everything else directly: ceremony against the
project's own wiring convention.
