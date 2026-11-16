---
name: expert-api-rest-tightened-input-keeps-old-requests-accepted
description: >-
  Recall of the "what an endpoint accepts is never tightened" part of
  expert-api-rest's compatibility bullet: a four-year-old customer creation
  endpoint is about to make an optional field required and to accept a phone
  only in international format, while old mobile app versions and two partner
  CRMs keep sending requests without the field and with national-format
  phones. The expert must require that those unchanged requests keep being
  accepted (server-side derivation or normalization, or the stricter rules
  only on a new version) instead of treating the stricter validation as a
  plain input check.
tags: [expert-api-rest, recall, compatibility, hardening]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-api-rest` sub-agent (Agent tool, `subagent_type: "vibe:expert-api-rest"`) with this brief plus the consultation request below.

Brief:

```
`POST /customers` has been live for four years. Our mobile app creates
customers through it (versions back to 3.2 are still installed, and users
update when they want), and so do two partner CRMs. Today `country` is
optional and `phone` is any string of digits, spaces, dashes and
parentheses. Our new SMS provider needs phone numbers in international
format, like `+33612345678`, so we want `POST /customers` to require
`country` and to accept `phone` only in international format, returning our
usual 422 validation error otherwise. About 40% of today's requests omit
`country`, and most phones arrive in national format, like `06 12 34 56 78`.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
