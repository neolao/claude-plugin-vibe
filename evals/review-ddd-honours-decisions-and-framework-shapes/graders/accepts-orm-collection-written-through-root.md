---
type: llm
focus: last_message
criteria: |
  `Product.variants` in fixtures/catalog/models.py is a SQLAlchemy
  `relationship`, public because the ORM requires it; `Product.add_variant`
  guards the unique SKU, and the only writer, `import_variants` in
  fixtures/catalog/import_job.py, calls `add_variant`.

  PASS if no `high` or `medium` severity Aggregate, Entity or Anemic model
  finding claims `Product`'s internals are exposed or written from outside,
  that the relationship should be private, or that the ORM base class or
  columns make `Product` a leaking domain type. A report with no findings at
  all passes.
  FAIL if `Product`, `Variant` or `import_variants` is flagged for one of
  those reasons at high or medium severity.
weight: 1
---

Does not call a collection the ORM imposes internals exposed when every
writer goes through the root's method.
