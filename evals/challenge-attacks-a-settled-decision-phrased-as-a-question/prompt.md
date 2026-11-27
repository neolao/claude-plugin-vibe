---
name: challenge-attacks-a-settled-decision-phrased-as-a-question
description: >-
  challenge must run the pass on a settled decision even when the argument is phrased as a question — a question mark alone does not make the choice open, so no redirect to /vibe:consult, the advocate launched and the closing block present
tags: [challenge, precision]
runs: 3
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Invoke the `vibe:challenge` skill (Skill tool, `skill: "vibe:challenge"`) with this argument, verbatim:

```
We picked SQLite as the local store of the desktop app — can you attack that? Reasons: single user, offline first, the app ships as one binary with nothing to install. Rejected: one JSON file per project, because it has no transactions and a project with more than a few thousand records took seconds to save in the prototype.
```

The workspace holds no project files. Report back exactly what the skill returned, in full.
