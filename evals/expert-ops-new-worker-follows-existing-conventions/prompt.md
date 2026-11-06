---
name: expert-ops-new-worker-follows-existing-conventions
description: >-
  Recall of the convention rule of expert-ops: a Python platform of seven
  services reads its configuration from one YAML file per environment
  through a typed settings module, logs logfmt lines through an in-house
  `log` module, ships through a GitLab pipeline whose stages every service
  shares and builds on the company's hardened base image. One worker is
  added. The expert must require that it reuse those conventions as they
  are — not prescribe environment-variable configuration, JSON logs, a new
  Dockerfile or a pipeline of its own as a second style.
tags: [expert-ops, recall, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our platform is seven Python services that have shipped the same way for
five years. Each reads its configuration from one YAML file per environment
(`config/<env>.yaml`) through the shared `settings` module, which types every
key and refuses to start on a missing one; secrets come from the same file,
which the deploy renders from the vault at release time. Every service logs
through the in-house `log` module: logfmt lines on stdout carrying a
`request_id`, which the log platform's dashboards and alerts are built on.
Every service is built by the same GitLab pipeline template (stages `lint`,
`test`, `image`, `deploy`) from the company's hardened `python-base` image,
and deployed by the platform team's Helm chart. We're adding a worker that
takes the image-resize requests the API drops on the internal queue, resizes
the upload and writes the result to the object store, so the API no longer
does it in the request. It needs the object store's bucket name and the
queue's address, and it will run as two replicas next to the API.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
