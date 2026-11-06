---
name: expert-ops-additive-message-field-needs-no-transition
description: >-
  Precision side of the deploy-compatibility bullet: a producer adds one
  optional field to the messages it publishes, every existing field kept
  as it is, while four pods roll out one at a time and two readers ignore
  fields they do not know. The expert must not demand a dual-publish
  period, a versioned message or topic, a feature flag or a multi-release
  sequence for an additive change — it may require the reader that will
  show the new field to cope with messages that do not carry it, and keeps
  the rest of its lists on the change itself.
tags: [expert-ops, precision, rolling-deploy]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our shipping service publishes a `parcel.dispatched` message to the
platform's message bus every time a parcel leaves the warehouse. We're
adding an `estimated_delivery` date to it, taken from the carrier's
response, so the tracking page can show it; every field the message carries
today keeps its name, type and meaning, and the carrier sometimes gives no
estimate, in which case the field is absent. The tracking service and the
nightly finance reconciliation job read these messages and both ignore
fields they do not know; the tracking page will show the estimate when it is
there. The shipping service runs as four pods rolled out one pod at a time
through the usual pipeline; the bus keeps messages for seven days.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
