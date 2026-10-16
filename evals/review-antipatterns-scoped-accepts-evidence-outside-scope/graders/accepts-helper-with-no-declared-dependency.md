---
type: llm
focus: last_message
criteria: |
  `slugify` in fixtures/orders/slugs.py builds a URL slug from stdlib
  pieces (`unicodedata`, `re`). The standard library has no slug function
  and fixtures/requirements.txt declares no slug library, so the helper
  duplicates nothing the project already has.

  PASS if no `high` or `medium` severity Wheel reinvention finding targets
  `slugify`. A report with no findings at all passes.
  FAIL if `slugify` is flagged at high or medium severity as reinventing a
  library the project does not declare.
weight: 1
---

Does not call a helper wheel reinvention when neither the standard library nor
the declared dependencies provide it.
