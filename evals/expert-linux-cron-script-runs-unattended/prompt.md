---
name: expert-linux-cron-script-runs-unattended
description: >-
  A script that worked when an engineer ran it from a terminal is being
  handed to cron: expert-linux must require what the unattended run changes —
  an explicit PATH instead of the interactive shell's, every call that could
  prompt (ssh, psql) made non-interactive so a run fails instead of hanging,
  and a lock so an hour-long run and the next ten-minute launch never overlap
  — as requirements, not as questions to the Product Owner.
tags: [expert-linux, recall, unattended]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-linux` sub-agent (Agent tool, `subagent_type: "vibe:expert-linux"`) with this brief plus the consultation request below.

Brief:

```
We're writing a bash script for our Linux ingestion servers. Every 10 minutes
it pulls the new CSV files a partner drops on their SFTP server (rsync over
ssh, key-based), loads each file into Postgres with `psql`, then moves the
file to an archive directory. It uses `psql` from `/opt/pgsql/bin` and our own
`csvcheck` tool from `/usr/local/bin`. An engineer has been running it by hand
from a terminal on the server for two weeks; it will now be scheduled from
cron. A normal run takes a few seconds; after the partner's monthly bulk
drop, one run can take over an hour.
```

Consultation request (send verbatim, appended to the brief):

```
Reply with three bulleted lists, ≤5 entries each, task-specific only (no generic checklists): REQUIREMENTS: (non-negotiable), RISKS: (domain pitfalls here), TEST SCENARIOS: (user action → expected result). Add a fourth list, OPEN QUESTIONS: (≤3), only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
