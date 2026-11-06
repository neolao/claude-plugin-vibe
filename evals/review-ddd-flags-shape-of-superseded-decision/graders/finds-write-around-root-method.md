---
type: llm
focus: last_message
criteria: |
  `Product.variants` in fixtures/catalog/models.py is a SQLAlchemy
  `relationship` the ORM requires public; `Product.add_variant` refuses a
  duplicate SKU. `import_variants` in fixtures/catalog/import_job.py
  appends a `Variant` to `product.variants` directly, around that rule.

  PASS if the reported findings include an `Aggregate` (or clearly
  equivalent category name, e.g. "Entity" or "Anemic model") finding on
  fixtures/catalog/import_job.py or fixtures/catalog/models.py whose ISSUE
  or SUGGESTION names `import_variants` (or import_job.py) as the writer
  bypassing `add_variant`.
  FAIL if no finding flags this write, or if the finding only blames the
  relationship for being public without naming the writer.
weight: 2
---

Reports the business write around the root's method, not the public
collection the ORM imposes.
