---
type: llm
focus: last_message
criteria: |
  fixtures/shop/settings.py is the Django settings module named by
  `DJANGO_SETTINGS_MODULE` in fixtures/manage.py. No file in the fixtures
  reads `ALLOWED_HOSTS`, `INSTALLED_APPS`, `MIDDLEWARE`, `ROOT_URLCONF`,
  `DATABASES`, `DEFAULT_AUTO_FIELD` or `USE_TZ`: Django does.

  PASS if no `high` or `medium` severity Cargo cult (or dead-configuration)
  finding targets any key of fixtures/shop/settings.py. A report with no
  findings at all passes.
  FAIL if a settings key is flagged at high or medium severity as unread
  or copied-in boilerplate.
weight: 1
---

Does not call settings cargo cult when their reader is the framework, not
the repository.
