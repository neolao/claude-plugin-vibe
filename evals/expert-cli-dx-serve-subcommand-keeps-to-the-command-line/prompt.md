---
name: expert-cli-dx-serve-subcommand-keeps-to-the-command-line
description: >-
  Recall side of the operations routing: a CLI gains a `serve` subcommand
  that starts a long-running server in the foreground, and the brief says
  the health endpoint, the Dockerfile and the restart policy are being
  written alongside. The command itself is expert-cli-dx's domain: it must
  fill its lists with the subcommand's flags, what reaches stdout and
  stderr while the server runs, and how the command exits when it cannot
  start — and leave the health endpoint, the image and the restart policy
  out of its REQUIREMENTS, since the scope sentence routes those to
  `expert-ops`.
tags: [expert-cli-dx, recall, ops-routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
Our CLI `agentd` has `agentd status` and `agentd sync`, both with ordinary
`--long` flags and a `--json` output. We're adding `agentd serve
--port <n> --config <file>`, which starts the agent's HTTP server in the
foreground and keeps running until it is stopped. Engineers run it from a
terminal during development; in production the container's entrypoint runs
it with no terminal attached and the orchestrator collects whatever it
prints. Alongside the command, the same work adds a `/healthz` endpoint to
the server, writes its Dockerfile and sets the deployment's restart policy.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
