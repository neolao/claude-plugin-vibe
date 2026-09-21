---
type: llm
focus: last_message
criteria: |
  orders-api 001's notes say it cannot start "until orders-sdk publishes
  v0.3.0". Step 4's done-vs-published rule makes that wait resolvable only by
  a matching pushed Git tag, and orders-sdk has none.

  PASS if the skill reports orders-api 001 as still blocked, and ties that to
  the version not having been released/tagged by orders-sdk.
  FAIL if it treats orders-api 001 as an eligible candidate, or explains it
  away with the state of an orders-sdk backlog item instead of a release.
weight: 2
---

Applies the done-vs-published distinction to the version-phrased blocker.
