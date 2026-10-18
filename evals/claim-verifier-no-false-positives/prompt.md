---
name: claim-verifier-no-false-positives
description: claim-verifier must return exactly `none` when every claim is sourced — a port claim reasonably supported by `PORT = 8000`, an approximate line reference, an opinion flagged as such, and a test result backed by the caller's command output
tags: [claim-verifier, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:claim-verifier` sub-agent (Agent tool, `subagent_type: "vibe:claim-verifier"`) with exactly this prompt:

```
Check the claims of the text below. Use: report of a run. Working directory: the current directory; the code is in `fixtures/`.

TEXT TO CHECK:
"The service listens on port 8000 (fixtures/config.py:3) and retries three times, around line 4 of the same file. Both tests pass. In my view three retries is on the high side for a startup check, but that is a judgement call for the Product Owner."

PROOFS PROVIDED BY THE CALLER:
$ python3 -m unittest -q
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Once the sub-agent returns, report its output back verbatim.
