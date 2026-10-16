---
name: expert-ui-ux-cli-brief-names-expert-cli-dx
description: >-
  Precision side of the command-line routing: a new CLI subcommand with a
  confirmation prompt, per-step progress output and a final summary is full
  of flows and feedback, so the one-line-reply test alone does not exclude
  it — but a terminal command is `expert-cli-dx`'s domain, whose checklist
  carries the CLI-specific form of those rules (a prompt on a non-TTY fails
  naming the flag instead of hanging a CI run). expert-ui-ux must decline in
  one line and name `expert-cli-dx` by id, since the experts never see the
  roster.
tags: [expert-ui-ux, precision, cli-routing]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-ui-ux` sub-agent (Agent tool, `subagent_type: "vibe:expert-ui-ux"`) with this brief plus the consultation request below.

Brief:

```
Our CLI tool `myctl` already has `myctl status` and `myctl backup`. We're
adding `myctl migrate`, which applies the pending database migrations in
order: it prints each migration's name as it starts and finishes, stops at
the first failure and says which one failed, asks for confirmation before a
migration that drops a column, and ends with a summary (applied, skipped,
failed). Engineers run it from a terminal; the deploy pipeline runs it from
CI with no one watching. There is no graphical interface in this change:
everything happens in the terminal.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
