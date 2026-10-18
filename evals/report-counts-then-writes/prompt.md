---
name: report-counts-then-writes
description: vibe:report (internal) must run its script for every operation — init, one incr/brick call per event as it happens, write at the end — and leave a statistics-only report under .vibe/reports/ with a self-ignoring .gitignore, closing with the 📊 line and the local-only sentence. Runs in Docker (Bash granted for the script); requires --scaffold and --allow-tools Bash.
tags: [report]
runs: 3
max_turns: 25
timeout_seconds: 300
allowed_tools: [Read, Skill, Bash]
---

You are the shared workflow of `vibe:feature`, playing a run on the project in the current directory (it has a `.vibe/` directory). The session model is `claude-sonnet-5-5`; the brief did not come from a backlog item.

Invoke the `vibe:report` skill (Skill tool, `skill: "vibe:report"`) with the argument `init feature claude-sonnet-5-5 no`, verbatim, and follow it from then on.

Then count these events in the order they happen, each at the moment it is listed here, through the skill's script:

1. the `clarify` brick is called, and it asks the user two questions;
2. the `review` brick is called and raises 5 findings;
3. the `review-classifier` brick is called: it drops 1 finding, merges 2, and keeps 1 high and 1 low;
4. the high finding sends the work back to the implementation framing — a new round starts;
5. 1 fix is made.

Finally invoke the skill again with the argument `write`, verbatim, and close exactly as the skill prescribes.

Report back the path of the report file and the closing lines you printed.
