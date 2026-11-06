---
type: llm
focus: last_message
criteria: |
  `QUEUE_URL`, `QUEUE_PREFETCH` and `QUEUE_RETRY_SECONDS` in
  fixtures/shop/config.py are read by no file in the fixtures;
  fixtures/requirements.txt declares no queue library and the project uses
  no framework that would read a config module on its own.

  PASS if the reported findings include a `Cargo cult` (or clearly
  equivalent category name) finding on these `QUEUE_*` constants, for
  configuration nothing reads.
  FAIL if no finding flags the unread `QUEUE_*` constants.
weight: 1
---

Reports the unread queue constants as Cargo cult: the framework exception
covers a reader the framework documents, not a module nothing reads.
