---
type: llm
focus: last_message
criteria: |
  About 40% of today's `POST /customers` requests omit `country`, and they
  come from mobile app versions still installed and from two partner CRMs
  that do not update on our schedule. Making `country` required turns each
  of those unchanged requests into a 422.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS requires that an existing
  client's request without `country` keeps being accepted, by any one
  concrete means: `country` stays optional on the existing endpoint (with
  the server deriving or defaulting it, or leaving the customer without a
  country), the required field exists only on a new API version or a new
  endpoint while the old one keeps accepting it until its clients have
  moved, or the reply names those old app versions or partners as what a
  required `country` would break and requires them to keep working.
  FAIL if the reply makes `country` required on the existing endpoint as a
  plain requirement (reject with 422 when it is missing) with no word on the
  clients that omit it today, or only says to "communicate the change" or
  "ask partners to update" without such a means.
weight: 2
---

Treats the newly required `country` as a tightening that existing clients
would feel, and keeps their unchanged requests accepted.
