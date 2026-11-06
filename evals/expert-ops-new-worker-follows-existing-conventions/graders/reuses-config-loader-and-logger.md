---
type: llm
focus: last_message
criteria: |
  The brief describes seven services that read their configuration from
  one YAML file per environment through a shared, typed `settings` module,
  and log logfmt lines through an in-house `log` module that the log
  platform's dashboards and alerts are built on. The expert's own checklist
  says the project's config loader and its logger and log format are
  reused as they are, even where it would pick otherwise.

  PASS if REQUIREMENTS has the worker read its bucket name and queue
  address through the existing `settings` module and YAML file (or "the
  project's config loader"), and log through the existing `log` module in
  its logfmt format with the request id — and prescribes no different
  mechanism for it.
  FAIL if any REQUIREMENTS entry prescribes, for the worker, configuration
  read from environment variables, a `.env` or example env file, or a
  settings mechanism of its own, or structured JSON logs or a logging
  library in place of the in-house `log` module. A different mechanism
  suggested only in RISKS as a gap or a later migration still passes.
weight: 2
---

Routes the worker's configuration through the existing `settings` module
and its logs through the in-house `log` module, instead of prescribing the
checklist's own env-var and JSON-log defaults as a second style.
