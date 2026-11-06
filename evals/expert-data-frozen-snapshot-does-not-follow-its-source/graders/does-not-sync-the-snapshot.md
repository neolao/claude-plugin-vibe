---
type: llm
focus: last_message
criteria: |
  The brief copies the product's name and unit price onto each invoice
  line precisely so that the invoice keeps saying what the customer was
  charged, whatever happens to the product afterwards: the copy is a
  snapshot frozen on purpose. The expert's own checklist says such a
  snapshot is not derived and must not follow its source.

  PASS if no REQUIREMENTS entry demands a mechanism that keeps the copied
  name or unit price in step with the `products` row — no trigger, no
  rebuild, no cascading update on a product change, no rule that the
  line's price must equal the product's current price — and the reply does
  not treat the copy as a duplication to remove. Requiring that the copy
  be taken in the same transaction as the invoice, that it never be
  updated after the invoice is issued, or that a changed product leave
  existing invoice lines untouched, is expected and passes; a RISKS entry
  on the copy being taken from a stale product read also passes.
  FAIL if REQUIREMENTS requires the invoice line's name or price to be
  updated when the product changes, a trigger or job that re-syncs the
  copy from `products`, or the removal of the copied columns in favour
  of a join on `products`.
weight: 2
---

Does not reach for a consistency mechanism on a deliberate snapshot: the
derived-value rule triggers on a copy kept current, and an invoice line
is frozen on purpose.
