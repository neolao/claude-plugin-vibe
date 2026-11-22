---
type: llm
focus: last_message
criteria: |
  The runtime writers of `_PLUGINS` (fixtures/storefront/registry.py) live
  in two other modules: fixtures/storefront/admin.py (`turn_off` calls
  `registry.disable`, `turn_on` calls `registry.enable`) and
  fixtures/storefront/tenants.py (`switch_to` calls `registry.disable`).

  Only a finding block (one starting with `FILE:`) counts. PASS if the
  finding that flags `_PLUGINS` (or its registry module) names both
  admin.py and tenants.py (file names or their functions `turn_off` /
  `turn_on` and `switch_to`) as places that write the registry.
  FAIL if no finding flags `_PLUGINS`, or if that finding names only one of
  the two modules, or none.
weight: 1
---

Grounds the finding in the writers found outside the registry module.
