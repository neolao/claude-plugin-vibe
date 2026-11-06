---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was the two files fixtures/core/events.py
  and fixtures/metrics/collector.py. Other files (fixtures/adapters/,
  fixtures/reporting/, fixtures/main.py, `.vibe/`) may be named inside a
  finding as evidence.

  PASS if every finding's `FILE:` line points to one of those two files,
  and every `MODULE:` line names the `metrics` module (whose only file is
  in scope).
  FAIL if any finding is anchored (`FILE:` or `MODULE:`) on a file or
  module outside the scope, for example a finding on
  fixtures/adapters/postgres_gateway.py or on the `reporting` module in
  its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the files given are reported on.
