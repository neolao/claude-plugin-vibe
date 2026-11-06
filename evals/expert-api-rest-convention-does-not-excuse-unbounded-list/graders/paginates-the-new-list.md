---
type: llm
focus: last_message
criteria: |
  The six existing list endpoints return their whole collection, which works
  because none holds more than about two hundred items. The new audit-event
  list starts at four million rows. The expert's own checklist reuses an
  API's existing conventions, but says an unbounded list stays a defect
  whatever the precedent.

  PASS if REQUIREMENTS requires the audit-event endpoint to be paginated
  (any form: page numbers, cursor, keyset), with the newest-first order and
  the user and date filters defined, and never presents returning the whole
  collection as acceptable for this endpoint.
  FAIL if the reply keeps the audit-event list unbounded to match the six
  existing lists, presents "return the full array like the other endpoints"
  as an option or a requirement, or leaves pagination of this endpoint as an
  open question for the Product Owner.
weight: 2
---

Requires the audit-event list to be paginated: the API's unpaginated
precedent does not excuse an unbounded response on a four-million-row table.
