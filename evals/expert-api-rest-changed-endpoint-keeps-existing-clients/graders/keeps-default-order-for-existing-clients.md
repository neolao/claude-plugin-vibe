---
type: llm
focus: last_message
criteria: |
  One partner pages through `GET /orders` every night with the list in its
  two-year-old default order, oldest first. Flipping the default to newest
  first changes what that unchanged request returns and what each page
  contains while the partner is paging.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS addresses the default order
  as a compatibility concern with a concrete means: the existing default
  stays and the warehouse asks for newest first through a sort parameter, or
  the new default lives only on a new version or endpoint, or the reply
  names the nightly paging partner as what a flipped default would break
  and requires it to keep working.
  FAIL if the reply changes the default order as a plain requirement
  ("the list returns newest first") with no word on the clients that depend
  on the current order, or never mentions the default order at all.
weight: 2
---

Treats the flipped default order as a change existing clients would feel,
and keeps the nightly paging partner's request returning what it did.
