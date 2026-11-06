---
type: llm
focus: last_message
criteria: |
  `DispatchTests.setUp` in fixtures/shop/tests/test_dispatch.py is the
  `unittest` fixture hook: the framework calls it before each test method.

  PASS if no `high` or `medium` severity Temporal coupling (or equivalent)
  finding targets `setUp` or the order between `setUp` and the test
  methods. A report with no findings at all passes.
  FAIL if that order is flagged at high or medium severity.
weight: 1
---

Does not call a lifecycle order the framework enforces temporal coupling.
