---
type: llm
focus: last_message
criteria: |
  In fixtures/orders/shipping.py, the comment `TODO(#88): costs come from a
  hard-coded table until the carrier client is available; do not call the
  carrier API from here yet.` sits above `shipping_cost`, which now returns
  `carrier.quote(...)`: the code below the marker calls the carrier API the
  marker says is not available yet. The marker carries a ticket reference.

  PASS if the reported findings include a finding anchored on
  fixtures/orders/shipping.py that flags this TODO as false or obsolete
  because the function already calls the carrier client, in the
  `Half-done migration` or `Stale marker` category (or a clearly equivalent
  name), and suggests removing it (or closing #88).
  FAIL if no finding flags this TODO, or if the report keeps it on the
  grounds that it carries a ticket reference.
weight: 1
---

Reports a ticketed TODO that the code beside it has made false: a ticket
reference does not protect a marker the new mechanism contradicts.
