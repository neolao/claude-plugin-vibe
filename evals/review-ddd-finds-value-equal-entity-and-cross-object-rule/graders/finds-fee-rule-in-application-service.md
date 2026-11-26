---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Domain service` (or clearly
  equivalent category name, e.g. "Domain isolation")
  finding on `CancelBooking.execute` in fixtures/booking/cancel.py for
  computing the late-cancellation fee (12-hour and 2-hour thresholds, the
  premium exemption) inside the use case that otherwise only loads, calls
  the domain, saves and charges, so the rule is invisible to the domain and
  not reusable. Where the SUGGESTION moves it (a domain service, a policy
  object, a method on `ClassSession` or `Member`) does not matter.
  FAIL if no finding flags the fee computation's placement in the use case.
weight: 2
---

Reports the business rule spanning the member, the session and the clock left
in an application service.
