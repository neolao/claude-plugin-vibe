---
name: expert-ops-convention-does-not-excuse-secret-in-image
description: >-
  Precision side of the convention rule: a platform's seven services have
  always shipped with a `config.json` baked into the image at build time,
  database passwords included, and print their logs as plain lines. The
  brief adds a service that calls a partner API with a newly issued key.
  "Reuse the existing conventions" must not become "copy the existing
  defect": expert-ops must still require the key to reach the process at
  runtime, never in the image, and must not make moving the seven existing
  services' passwords out of their images a requirement of this change.
tags: [expert-ops, precision, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ops` sub-agent (Agent tool, `subagent_type: "vibe:expert-ops"`) with this brief plus the consultation request below.

Brief:

```
Our seven Node services have shipped the same way for years: the pipeline
builds one image per environment with `--build-arg ENV=<env>`, and the
Dockerfile copies `config/<env>.json` into the image — hostnames, feature
switches, the database password and the Redis password included; the
service reads that file at startup. Logs are plain `console.log` lines
collected by the platform. The images live in the company registry, which
every engineer and the CI runners can pull from. We're adding an eighth
service that sends shipment notifications through a partner's API; the
partner has just issued us an API key for production and another for
staging. The service needs the partner's base URL, a per-call timeout and
the key. It runs as one replica and goes through the same pipeline as the
others.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
