---
type: llm
focus: last_message
criteria: |
  The subject prefix `"[Shop] "` is written as `SUBJECT_PREFIX` in
  fixtures/notifications/templates.py and as a literal in
  `order_reference` of fixtures/mail/parser.py, which strips it from reply
  subjects. fixtures/tests/test_parser.py sends the subject produced by
  `order_confirmed` through the parser, so changing the prefix on one side
  fails the suite; the round-trip covers the confirmation subject only,
  not the one `order_shipped` produces.

  PASS if no `high` or `medium` severity finding names the subject prefix,
  `SUBJECT_PREFIX` or `order_reference`. A `low` finding on it passes (for
  example the missing round-trip on `order_shipped`), and so does a report
  that does not mention it.
  FAIL if the subject prefix is flagged at high or medium severity.
weight: 2
---

Caps a copy guarded by a round-trip test at `low` at most: the test reaches
both the template and the parser, so a prefix change fails the suite; at
worst the missing `order_shipped` round-trip is a `low`.
