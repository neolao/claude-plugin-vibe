---
type: llm
focus: last_message
criteria: |
  `SESSION_CACHE` in fixtures/web/cache.py is a module-level dict written
  from fixtures/web/login.py (`[token] = user`), fixtures/web/logout.py
  (`pop`) and fixtures/web/admin.py (`clear`), under the
  `ThreadingHTTPServer` of fixtures/web/server.py.

  PASS if the reported findings include a `Mutable global state` (or
  clearly equivalent category name) finding on `SESSION_CACHE` with
  SEVERITY `medium`.
  FAIL if no finding flags `SESSION_CACHE` as mutable global state, or if
  that finding carries SEVERITY `high` or `low`.
weight: 2
---

Reports the shared dict at `medium`: the global is the cost this agent
reports; the race under the threaded server is review-correctness' bug.
