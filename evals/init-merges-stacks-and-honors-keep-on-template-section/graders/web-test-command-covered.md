---
type: llm
focus:
  source: file
  path: CLAUDE.md
criteria: |
  Look only at the Definition of Done line that starts "Tests cover the
  nominal path" and the command(s) it names.
  PASS if that line names a command for the Python suite (pytest, or an
  equivalent) AND a command that runs the `web/` front-end suite (for
  example `npm test` run in `web/`, `npm --prefix web test`,
  `cd web && npm test`, or `vitest run` scoped to `web/`).
  FAIL if the line names only the Python command, or only the web command.
weight: 2
---

The repo has two stacks, each with its own test runner. The Definition of
Done's test line must cover both, not only the Python suite the stale
`CLAUDE.md` knew about.
