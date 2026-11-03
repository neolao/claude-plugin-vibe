---
name: expert-ops-renamed-field-survives-rolling-deploy
description: >-
  Recall of the rolling-deploy item of expert-ops: a producer renames a field
  of the messages it publishes while three of its four pods keep running the
  old version during the rollout, and a nightly reporting job owned by another
  team reads the same messages. The expert must require that old and new
  versions coexist, that the existing consumer keeps working on the new data,
  and a rollback path that still holds once new-format messages are in the
  queue.
tags: [expert-ops, recall, rolling-deploy]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our shipping service publishes a `parcel.dispatched` message to the platform's
message bus every time a parcel leaves the warehouse. The message carries a
`carrier` field with the carrier's name as free text ("DHL Express", "dhl",
"Colissimo"). We're replacing it with a `carrier_code` field holding one of a
fixed list of codes, so the tracking page can show the right logo. The tracking
service and the nightly finance reconciliation job, which belongs to another
team, both read these messages today. The shipping service runs as four pods
and is rolled out one pod at a time through the usual pipeline; the bus keeps
messages for seven days. We want this live before the end of the month.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
