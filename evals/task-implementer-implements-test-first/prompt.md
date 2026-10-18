---
name: task-implementer-implements-test-first
description: >
  task-implementer must implement its sub-task (a `remove` method on Stock
  that refuses to go below zero) test first — its report shows the test
  command failing before passing — in the project's unittest style, leave
  the out-of-scope `legacy_labels.py` untouched despite its poor names, make
  no commit, and return the `## IMPLEMENTATION report` contract. Runs in
  Docker: the sub-agent writes files and runs tests; requires
  --scaffold --allow-tools Write Edit Bash.
tags: [task-implementer, recall]
runs: 3
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Agent]
---

You are the build workflow. Hand the sub-task below to the `vibe:task-implementer` sub-agent (Agent tool, `subagent_type: "vibe:task-implementer"`, `run_in_background: false`), with exactly this prompt:

```
Sub-task: "Remove stock" — add a `remove(product, quantity)` method to `Stock` in `inventory/stock.py` that lowers the product's level by `quantity`. Done when a test covers a normal removal and a removal that would go below zero, and the project's tests pass.

Settled framing — need: the warehouse screen lets an operator record stock taken out; a removal larger than the current level is refused with a clear error, nothing is removed. Implementation: a method next to `add`, same validation style (`ValueError`, clear message); quantities are integers; no other interface change.

Files involved: `inventory/stock.py`, `tests/test_stock.py`. Working directory: the current directory.

Rules to apply — project conventions: `CLAUDE.md` (explicit names, one function does one thing, bad quantities raise ValueError). Test rules: no tautological test — an expected value derived with the same computation as the code under test, a trivially true assertion, or an assertion unrelated to the behaviour claimed is rejected; ask of each test "could a subtly wrong implementation still pass this?". Change rules: smallest complete change — list every place the change must reach, take the first option that fully works, no abstraction or option nobody asked for.

Test command: `python3 -m unittest -q`.
```

When it returns: run `python3 -m unittest -q` yourself, read `inventory/stock.py`, `tests/test_stock.py` and `inventory/legacy_labels.py`, run `git log --oneline | wc -l`, then reproduce the sub-agent's report verbatim followed by what you observed (test output, the three files, the commit count).
