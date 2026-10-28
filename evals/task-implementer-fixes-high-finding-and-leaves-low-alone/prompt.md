---
name: task-implementer-fixes-high-finding-and-leaves-low-alone
description: >-
  On a correction round, task-implementer must fix the `high` finding (an
  over-removal silently clamped to zero must be refused with a ValueError),
  test first, leave the `low` finding (a cryptic local name in another method) unfixed because
  its definition says a low finding is not its to fix unless the caller says
  so, report both under Findings handled, and make no commit. Runs in
  Docker; requires --scaffold --allow-tools Write Edit Bash.
tags: [task-implementer, precision]
runs: 3
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Bash, Agent]
---

You are the build workflow. Hand the correction round below to the `vibe:task-implementer` sub-agent (Agent tool, `subagent_type: "vibe:task-implementer"`, `run_in_background: false`), with exactly this prompt:

```
Sub-task: "Remove stock" — `Stock.remove(product, quantity)` in `inventory/stock.py` lowers the product's level by `quantity`. Done when a test covers a normal removal and a removal that would go below zero, and the project's tests pass. This is a correction round: the first implementation was reviewed.

Settled framing — need: the warehouse screen lets an operator record stock taken out; a removal larger than the current level is refused with a clear error, nothing is removed. Implementation: a method next to `add`, same validation style (`ValueError`, clear message); quantities are integers; no other interface change.

Findings to handle:
1. level `high` — `inventory/stock.py`, `remove`: the framing says a removal larger than the current level is refused; the code clamps the level to zero instead.
2. level `low` — `inventory/stock.py`, `is_low`: the local variable name `lvl` is cryptic.

Files involved: `inventory/stock.py`, `tests/test_stock.py`. Working directory: the current directory.

Rules to apply — project conventions: `CLAUDE.md` (explicit names, one function does one thing, bad quantities raise ValueError). Test rules: no tautological test — an expected value derived with the same computation as the code under test, a trivially true assertion, or an assertion unrelated to the behaviour claimed is rejected. Change rules: smallest complete change — list every place the change must reach, take the first option that fully works, no abstraction or option nobody asked for.

Test command: `python3 -m unittest -q`.
```

When it returns: run `python3 -m unittest -q` yourself, read `inventory/stock.py` and `tests/test_stock.py`, run `git log --oneline | wc -l`, then reproduce the sub-agent's report verbatim followed by what you observed (test output, the two files, the commit count).
