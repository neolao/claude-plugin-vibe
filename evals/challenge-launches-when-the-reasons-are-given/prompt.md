---
name: challenge-launches-when-the-reasons-are-given
description: >-
  challenge must launch the advocate at once, without asking anything, when the argument already carries the reasons for the choice and the alternatives rejected; the account handed to the advocate carries those alternatives, and every objection comes back with an opinion under the closing block
tags: [challenge, precision]
runs: 3
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Invoke the `vibe:challenge` skill (Skill tool, `skill: "vibe:challenge"`) with this argument, verbatim:

```
We picked SQLite as the local store of the desktop app. Reasons: single user, offline first, the app ships as one binary with nothing to install, and every project fits in a few hundred thousand rows. Rejected: PostgreSQL, because the installer would have to bundle and supervise a server process; one JSON file per project, because it has no transactions and a project with more than a few thousand records took seconds to save in the prototype.
```

The workspace holds no project files. Report back exactly what the skill returned, in full.
