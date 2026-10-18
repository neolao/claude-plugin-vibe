---
name: rewrite-direct-mode-returns-text-without-asking
description: vibe:rewrite in `mode: direct` must return the rewritten paragraph itself (no before/after table, no AskUserQuestion, nothing written), still run the meaning-preservation check through one sub-agent, keep every fact of the original, and close with the direct-mode block
tags: [rewrite, direct-mode]
runs: 3
max_turns: 12
timeout_seconds: 300
allowed_tools: [Read, Skill, Agent]
---

You are a vibe workflow about to show the Product Owner this report paragraph. Invoke the `vibe:rewrite` skill (Skill tool, `skill: "vibe:rewrite"`) with this argument, verbatim:

```
mode: direct
Reader: the Product Owner of the project, who does not read code.
Implementation of the export of the monthly report in CSV format has been completed by the addition of a dedicated module, the invocation of which is performed by the admin page, with the sorting of the lines by ascending date being carried out prior to serialization. Verification of the behaviour was conducted through the execution of the test suite, with a passing result for all four tests, and through a manual download from a locally-run instance. There is no modification of the signature of the function that the admin page calls.
```

Then report back exactly what the skill returned, in full.
