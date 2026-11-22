---
type: llm
focus: last_message
criteria: |
  `_PLUGINS` in fixtures/storefront/registry.py is a module-level dict the
  project wrote itself (no plugin framework is involved). It is filled at
  import time by the `plugin` decorator, then written again while the app
  runs: `disable` is called from fixtures/storefront/admin.py (`turn_off`)
  and fixtures/storefront/tenants.py (`switch_to`), `enable` from
  fixtures/storefront/admin.py (`turn_on`).

  PASS if the reported findings include a `Mutable global state` (or
  clearly equivalent category name) finding on `_PLUGINS` (or on the
  registry module that holds it) with SEVERITY `medium`.
  FAIL if no finding flags `_PLUGINS` as mutable global state, if that
  finding carries SEVERITY `high` or `low`, or if the report treats the
  registry as an exempt plugin-system registry and stays silent on it.
weight: 2
---

Does not stretch the plugin-system exemption to a hand-rolled registry that
other modules rewrite at runtime.
