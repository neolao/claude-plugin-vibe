---
type: llm
focus: last_message
criteria: |
  The glossary's "Order total" is computed once, by `calculate_total` in
  fixtures/core/pricing.py. fixtures/api/http.py returns it,
  fixtures/adapters/postgres_gateway.py stores and reads it,
  fixtures/jobs/nightly.py sums the stored values: three modules reference
  the concept, none recomputes it.

  PASS if no `high` or `medium` severity Responsibility spread finding
  targets "Order total", `calculate_total` or `total_cents`. A report with
  no findings at all passes.
  FAIL if the concept is reported as spread at high or medium severity.
weight: 1
---

Does not call a concept referenced from several modules, but computed in
one, responsibility spread.
