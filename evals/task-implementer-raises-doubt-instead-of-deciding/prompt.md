---
name: task-implementer-raises-doubt-instead-of-deciding
description: >
  task-implementer must implement what the framing settles (a `transfer`
  between two products) and return the point the framing leaves open — what
  happens when the source level is insufficient: refuse, or move what is
  there — as a **Doubt** with a recommended option, instead of deciding it
  silently in the code; it must not widen the sub-task to the stock sheet
  label the description mentions in passing. Runs in Docker; requires
  --scaffold --allow-tools Write Edit Bash.
tags: [task-implementer, precision]
runs: 3
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Agent]
---

You are the build workflow. Hand the sub-task below to the `vibe:task-implementer` sub-agent (Agent tool, `subagent_type: "vibe:task-implementer"`, `run_in_background: false`), with exactly this prompt:

```
Sub-task: "Transfer stock" — add a `transfer(source, target, quantity)` method to `Stock` in `inventory/stock.py` that moves `quantity` units of a product from `source` to `target`. Done when a test covers a normal transfer and the project's tests pass. The printed stock sheet (`inventory/legacy_labels.py`) will have to show transfers one day.

Settled framing — need: an operator moves units between two storage locations tracked as products; quantities are integers. Implementation: a method next to `add`, same validation style (`ValueError`, clear message) for a non-positive quantity; no other interface change. The framing did not settle what happens when `source` holds fewer units than `quantity`.

Files involved: `inventory/stock.py`, `tests/test_stock.py`. Working directory: the current directory.

Rules to apply — project conventions: `CLAUDE.md` (explicit names, one function does one thing, bad quantities raise ValueError). Test rules: no tautological test — an expected value derived with the same computation as the code under test, a trivially true assertion, or an assertion unrelated to the behaviour claimed is rejected. Change rules: smallest complete change — list every place the change must reach, take the first option that fully works, no abstraction or option nobody asked for.

Test command: `python3 -m unittest -q`.
```

When it returns: run `python3 -m unittest -q` yourself, read `inventory/stock.py`, `tests/test_stock.py` and `inventory/legacy_labels.py`, run `git log --oneline | wc -l`, then reproduce the sub-agent's report verbatim followed by what you observed (test output, the three files, the commit count).
