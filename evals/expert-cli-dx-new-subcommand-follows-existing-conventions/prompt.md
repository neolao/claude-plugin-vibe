---
name: expert-cli-dx-new-subcommand-follows-existing-conventions
description: >-
  Recall of the convention rule of expert-cli-dx: a four-year-old Go CLI
  uses single-dash long flags, `-o table|json` on every command and a
  documented exit code 2 for "not found" that scripts branch on. One
  subcommand is added. The expert must require that it reuse those
  conventions as they are — not prescribe `--double-dash` flags, a new
  `--json` switch or a different meaning for exit code 2 — and still give
  the new subcommand its own distinct non-zero exit code on failure.
tags: [expert-cli-dx, recall, conventions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
Our Go CLI `fleet` has had nine subcommands for four years (`fleet nodes`,
`fleet cordon <node>`, `fleet reboot <node>`...). Every flag is a single-dash
long flag (`-region eu`, `-timeout 30s`, `-dry-run`), every command takes
`-o table` or `-o json` for its output, errors print as `error: <message>` on
stderr, and exit code 2 means "the node does not exist" — the autoscaler's
scripts branch on it. We're adding `fleet drain <node>`, which moves the
workloads off a node and then cordons it. Engineers run it from a terminal;
the autoscaler's scripts will run it unattended before scaling a node down.
Nothing else in the CLI changes.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
