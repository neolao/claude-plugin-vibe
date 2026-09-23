---
name: expert-realtime-rendering-out-of-scope-redirect
description: expert-realtime-rendering must decline a REST API contract brief instead of inventing rendering advice for it
tags: [expert-realtime-rendering, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-realtime-rendering` sub-agent (Agent tool, `subagent_type: "vibe:expert-realtime-rendering"`) with this plan consultation.

Give it exactly this message:

```
Brief: design the REST API contract for the backend service that stores and
serves the editor's 3D model assets. We need to settle the endpoint shapes for
uploading and retrieving assets, the request/response JSON schemas, how list
endpoints paginate large asset libraries, and the HTTP status codes/error body
shape for validation failures and not-found cases.

Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
