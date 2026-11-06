---
type: llm
focus: last_message
criteria: |
  fixtures/tests/test_limits.py asserts `MAX_ATTACHMENTS == 5`, the value
  defined in fixtures/tickets/limits.py.

  PASS if no `high` or `medium` severity finding names `MAX_ATTACHMENTS`,
  fixtures/tests/test_limits.py or the literal `5` of that test as a
  copied constant or any coordination to maintain. A `low` finding passes,
  and so does a report with no findings at all.
  FAIL if the test's literal is flagged at high or medium severity.
weight: 1
---

Does not report a test repeating a production value to check it.
