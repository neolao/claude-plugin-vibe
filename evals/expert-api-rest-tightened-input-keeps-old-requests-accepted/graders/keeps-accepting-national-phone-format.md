---
type: llm
focus: last_message
criteria: |
  Most phones reach `POST /customers` in national format (`06 12 34 56 78`),
  which the endpoint has accepted for four years. Accepting only the
  international format turns each of those unchanged requests into a 422,
  although the SMS provider's need is about what the server sends on, not
  about what clients send in.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS requires that the existing
  endpoint keeps accepting the phone formats it accepts today, by any one
  concrete means: the server normalizes a national-format phone to
  international format itself (from the country, a default, or the
  account), it stores the phone as received and converts it when sending to
  the SMS provider, or the international-only rule exists only on a new API
  version or a new endpoint while the old one keeps accepting today's
  formats. A reply that also says what happens when a phone cannot be
  normalized (stored but not sent by SMS, flagged) still passes.
  FAIL if the reply requires the existing endpoint to reject a
  national-format phone with 422 as a plain requirement, with no means that
  keeps today's requests accepted.
weight: 2
---

Keeps national-format phones accepted on the existing endpoint and moves
the SMS provider's format to the server side, or to a new version.
