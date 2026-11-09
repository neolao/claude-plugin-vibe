---
type: llm
focus: last_message
criteria: |
  `is_expired` in fixtures/sessions/store.py subtracts `session["created_at"]`
  (timezone-aware, UTC, from `new_session`) from `datetime.now()` (naive):
  Python raises `TypeError: can't subtract offset-naive and offset-aware
  datetimes`, so `current_user` crashes for every logged-in user.

  PASS if the findings include one on `is_expired` (category `Numbers/time`
  or equivalent) saying the naive and aware datetimes cannot be subtracted
  (or that the comparison is wrong by the timezone offset), with SEVERITY
  `high` or `medium`.
  FAIL if no finding reports this, or it is rated `low`.
weight: 2
---

Reports the naive/aware datetime mix on the session expiry check.
