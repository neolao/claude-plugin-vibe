---
type: llm
focus: last_message
criteria: |
  `ShopPreferences` in fixtures/settings/preferences.py holds four fields
  the admin page sets, and `update_preferences` in fixtures/settings/admin.py
  copies the form into them and saves; no rule, transition or total is
  computed anywhere over those fields.

  PASS if no `high` or `medium` severity Anemic model, Entity or Aggregate
  finding claims `ShopPreferences` is anemic, needs intention-revealing
  methods, or has its behaviour in `update_preferences`. A report with no
  findings at all passes.
  FAIL if the settings module is flagged for one of those reasons at high
  or medium severity.
weight: 1
---

Does not call a CRUD module with no rule over its data anemic.
