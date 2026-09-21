---
type: llm
focus: last_message
criteria: |
  The `repository` function in fixtures/test_order_repository.py is
  decorated with `@pytest.fixture` and named as a parameter by three tests
  in the same file — pytest injects it by name, so nothing calls it
  directly.

  PASS if no `high` or `medium` severity finding calls this function unused,
  uncalled, or dead.
  FAIL if it is flagged as Dead code (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a pytest fixture function uncalled.
