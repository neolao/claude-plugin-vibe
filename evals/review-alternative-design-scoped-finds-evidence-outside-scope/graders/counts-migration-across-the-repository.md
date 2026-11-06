---
type: llm
focus: last_message
criteria: |
  The agent's definition counts the migration in files by grepping the
  callers and the sibling switches wherever they sit, scope included or
  not. A registry for the discount kinds moves at least
  fixtures/orders/discount.py, fixtures/invoicing/line_label.py and
  fixtures/admin/promo_form.py.

  PASS if the finding on the discount kinds gives its migration as a
  number of files that includes at least one file outside fixtures/orders/
  (named or counted), so the cost is not understated to the in-scope file
  alone.
  FAIL if the migration is counted on fixtures/orders/ only, or is not
  given as a file count.
weight: 1
---

Counts the migration over the whole repository, not over the path under
review.
