---
type: llm
focus: last_message
criteria: |
  `reserve` in fixtures/orders/reservations.py reads the level through
  `level`, compares it with `qty`, then writes `available - qty` through
  `set_level`, with no lock; fixtures/app/server.py (outside the scope) is
  a `ThreadingHTTPServer`, one thread per request, and `/reserve` calls
  `reserve` directly.

  PASS if the reported findings include a `Race` (or clearly equivalent
  category name) finding on `reserve` describing two concurrent
  reservations that both pass the check and together take more than the
  stock holds (or overwrite each other's write), naming the thread-pool
  server (fixtures/app/server.py or `ThreadingHTTPServer`) as what makes
  the calls overlap.
  FAIL if no finding flags this check-then-act.
weight: 2
---

Reports the check-then-act on the shared levels. reservations.py alone
shows two helper calls; only app/server.py, outside the scope, shows that
two requests run at once.
