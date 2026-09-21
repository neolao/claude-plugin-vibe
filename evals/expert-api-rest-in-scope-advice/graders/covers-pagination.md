---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  brief, that the comment-listing endpoint must be paginated (with filtering
  and/or sorting) because a post can have tens of thousands of comments — an
  unbounded/unpaginated response is called out as a defect for this specific
  endpoint.
  FAIL if pagination is missing entirely, or only mentioned as a generic
  best-practice aside without being tied to the large-comment-count scenario
  in the brief.
weight: 2
---

Names pagination of the comment-listing endpoint as a concrete requirement or
risk, tied to the brief's "tens of thousands of comments" detail.
