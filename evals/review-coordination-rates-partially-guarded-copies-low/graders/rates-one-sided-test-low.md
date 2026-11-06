---
type: llm
focus: last_message
criteria: |
  The subject prefix `"[Shop] "` is written as `SUBJECT_PREFIX` in
  fixtures/notifications/templates.py and as a literal in
  `order_reference` of fixtures/mail/parser.py, which strips it from reply
  subjects. fixtures/tests/test_templates.py asserts `SUBJECT_PREFIX ==
  "[Shop] "` and checks a confirmation subject, but no test exercises the
  parser against a subject the templates produced: the guard covers one
  side only.

  PASS if no `high` or `medium` severity finding names the subject prefix,
  `SUBJECT_PREFIX` or `order_reference`. A `low` finding on it passes, and
  so does a report that does not mention it.
  FAIL if the subject prefix is flagged at high or medium severity.
weight: 2
---

Caps a partially guarded copy at `low`: a test on one side only is a
partial guard, and the agent's rule says a partial guard is `low`, saying
what is missing (here, a round-trip test from the template to the parser).
