---
type: llm
focus: last_message
criteria: |
  The brief says the partners who integrated last year were promised that
  shipping this will not break anything currently working for them.

  PASS if at least one entry of REQUIREMENTS, RISKS, or TEST SCENARIOS says
  how that promise is kept for the existing partner integrations — any one
  concrete means is enough: the change is additive only, existing endpoints
  or fields stay unchanged (not repurposed or removed), a versioning
  strategy for the API contract, or a test scenario checking that an
  endpoint partners already use behaves as before.
  FAIL if backward compatibility is missing entirely, or if the only mention
  is a generic "be careful with breaking changes" remark that names no
  existing integration and no means of keeping it working.
weight: 2
---

Names how backward compatibility is kept for the existing partner
integrations, tied to the brief's "promised last year's partners" detail.
