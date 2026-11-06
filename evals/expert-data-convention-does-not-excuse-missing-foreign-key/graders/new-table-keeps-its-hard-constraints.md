---
type: llm
focus: last_message
criteria: |
  The existing tables have no foreign keys and store amounts as `double
  precision`; the new `invoices` table carries money that the accounting
  export sums, and a link to a customer. The expert's own checklist reuses
  a schema's existing conventions, but says money as a float and a
  relation without its foreign key stay defects whatever the precedent.

  PASS if REQUIREMENTS requires both, for the new table: an exact amount
  type (`numeric`/`decimal` with a scale, or integer minor units — never
  `double precision`/`float`), and a foreign key from `invoices` to
  `customers` enforced by the database — and never presents "no foreign key
  and a double, like the other tables" as acceptable for this table.
  FAIL if the reply stores the invoice amount as a float to match the
  existing tables, leaves the customer link unenforced because the other
  tables have no foreign keys, presents matching the existing behaviour as
  an option or a requirement, or leaves either point as an open question
  for the Product Owner.
weight: 2
---

Requires an exact amount type and a database-enforced foreign key on the
new table: the schema's float-and-no-foreign-key precedent does not excuse
an invoice total that drifts by a cent or an invoice pointing at no
customer.
