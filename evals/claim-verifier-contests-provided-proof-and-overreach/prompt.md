---
name: claim-verifier-contests-provided-proof-and-overreach
description: >-
  claim-verifier must contest a proof the caller provides when the cited source contradicts it ("Ran 3 tests" while fixtures/test_sync.py holds 2), flag a conclusion the cited lines do not allow (a record that keeps failing is "reported to the caller as failed", while sync.py:15-16 silently drops it), and leave the correct doubling-backoff claim alone. Bash granted so the agent may re-run the cheap unit test.
tags: [claim-verifier, recall, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Bash, Agent]
---

Invoke the `vibe:claim-verifier` sub-agent (Agent tool, `subagent_type: "vibe:claim-verifier"`) with exactly this prompt:

```
Check the claims of the text below. Use: report of a run. Working directory: the current directory; the code is in `fixtures/`.

TEXT TO CHECK:
"A record that keeps failing is attempted three times and then reported to the caller as failed (fixtures/sync.py:10-16). The wait after each failed attempt doubles each time (fixtures/sync.py:16). All 3 tests pass."

PROOFS PROVIDED BY THE CALLER:
$ python3 -m unittest -q
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

Once the sub-agent returns, report its output back verbatim.
