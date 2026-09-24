---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags the `except requests.RequestException as exc:
  raise SupplierError(sku) from exc` in `SupplierClient.stock_level`
  (fixtures/inventory/supplier.py) as swallowing the error or losing its
  context. It chains the original exception with `from exc` and its message
  names the SKU.
  A finding on the same function about the timeout value does not count
  against this grader, and neither does a report that mentions this wrapping
  only to say it is fine.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the chained `SupplierError` in supplier.py.
