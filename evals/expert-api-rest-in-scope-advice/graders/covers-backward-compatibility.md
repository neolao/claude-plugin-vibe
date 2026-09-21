---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  brief, that shipping the new endpoints must not break the partners already
  integrated last year — e.g. additive-only changes, no repurposing/removing
  existing fields or behavior, or a versioning strategy for the API contract.
  FAIL if backward compatibility is missing entirely, or only a vague "be
  careful with breaking changes" remark with no connection to the brief's
  existing-partners detail.
weight: 2
---

Names backward compatibility for existing partner integrations as a concrete
requirement or risk, tied to the brief's "promised last year's partners"
detail.
