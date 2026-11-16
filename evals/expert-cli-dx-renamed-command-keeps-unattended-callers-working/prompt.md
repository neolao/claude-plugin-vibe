---
name: expert-cli-dx-renamed-command-keeps-unattended-callers-working
description: >-
  Compatibility meets the destructive-operation guard: `vault rm` is renamed
  `vault delete` and gains a confirmation prompt, while three teams' CI
  cleanup jobs call `vault rm <name>` with no terminal attached. The expert
  must keep the old name working through a transition, keep the unchanged
  unattended invocation deleting without hanging or failing in this change,
  and make the new command fail fast on a non-TTY without its skip flag.
tags: [expert-cli-dx, recall, compatibility, destructive]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-cli-dx` sub-agent (Agent tool, `subagent_type: "vibe:expert-cli-dx"`) with this brief plus the consultation request below.

Brief:

```
Our secrets CLI `vault` has `vault create`, `vault list` and `vault rm
<name>`, all with ordinary `--long` flags. `vault rm` has existed for five
years: it deletes the secret at once, prints nothing and exits 0. Last month
an engineer deleted a production secret by typing the wrong name, so we are
renaming `vault rm` to `vault delete`, to match `create` and `list`, and
`delete` will ask "Delete secret <name>? [y/N]" before deleting anything.
The CI pipelines of three teams call `vault rm <name>` in their nightly
cleanup jobs, which run with no terminal attached. We don't control when
those teams change their pipelines.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
