---
type: llm
focus: last_message
criteria: |
  The fixtures use only legitimate patterns that superficially resemble
  hygiene violations without being one:
  - `record_event` in fixtures/api.py looks unused within the package but is
    part of the module's declared `__all__` public API, consumed by other
    services — not dead code.
  - the `repository` pytest fixture in fixtures/test_order_repository.py
    looks like an uncalled function but is injected into tests by pytest via
    fixture-name matching — a test helper used by convention, not unused.
  - `# TODO(JIRA-4231): ...` in fixtures/order_repository.py is a TODO with an
    attached ticket reference — not a stale marker.
  - `test_calculate_discounted_total_applies_promo` and
    `test_calculate_discounted_total_without_promo` in
    fixtures/test_order_repository.py share a similar arrange-act-assert
    shape but each exercises a distinct branch (with/without promo) —
    legitimate test repetition that aids readability, not copy-paste
    duplication with real divergence risk.
  - `@pytest.mark.skip(...)` on `test_is_active_returns_false_when_missing`
    is a skipped test, which is `review-tests`' dead-test-code check, not
    review-hygiene's.

  PASS if the response reports no `high` or `medium` severity Dead code,
  Leftover, Stale marker, or Duplication finding on any of the five patterns
  above — either no findings at all, or only `low` severity style notes
  unrelated to them.
  FAIL if it flags `record_event` as dead code, the `repository` fixture as
  unused, the ticketed TODO as stale, the two promo tests as duplicated, or
  the `skip` marker as a hygiene issue.
weight: 2
---

Does not invent hygiene findings on code that already follows the idiomatic,
justified pattern for each category.
