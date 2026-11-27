---
name: requirements-reviewer-finds-a-nice-gap-and-honors-the-decision-over-the-criterion
description: >-
  requirements-reviewer must report the ✨ NICE dry-run decision left out as a gap quoting its priority, while the 24-month limit the 🔒 MUST decision settled over the item's 12-month criterion is neither a gap nor an ambiguity
tags: [requirements-reviewer, recall, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:requirements-reviewer` sub-agent (Agent tool, `subagent_type: "vibe:requirements-reviewer"`) with exactly this prompt:

```
Check the deliverable against the request. Type of use: code against its brief.

REQUEST: the backlog item `fixtures/REQUEST.md` in the current directory, and the need framing's decisions, quoted verbatim:

### Decisions made
- **Age limit** (🔒 MUST): 24 months, not 12 — the finance team keeps two fiscal years in the live table
- **Night run** (⚖️ SHOULD): the existing nightly scheduler runs it at 02:00 (source: fixtures/scheduler.py:1)
- **Dry run** (✨ NICE): `archive_old(ledger, today, dry_run=False)` reports what it would move without moving it

DELIVERABLE (files changed since the baseline): `fixtures/archive.py`, `fixtures/scheduler.py` and `fixtures/test_archive.py`.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.
