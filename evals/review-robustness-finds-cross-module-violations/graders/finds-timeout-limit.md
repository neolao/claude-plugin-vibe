---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Timeout/limit` (or clearly
  equivalent category name) finding for the supplier HTTP call having no
  timeout by default: `SupplierClient.stock_level`
  (fixtures/inventory/supplier.py) passes `timeout=settings.SUPPLIER_TIMEOUT`,
  and `SUPPLIER_TIMEOUT` (fixtures/inventory/settings.py) is `None` whenever
  the environment variable is unset, so `requests` waits forever on a
  supplier that stops answering. The finding may be anchored in settings.py
  or supplier.py, as long as it names the `None` default.
  FAIL if no finding flags this missing default timeout.
weight: 1
---

Reports the `None` default of `SUPPLIER_TIMEOUT` reaching `session.get`.
supplier.py alone passes a timeout; only settings.py shows it can be `None`.
