---
type: llm
focus: last_message
criteria: |
  fixtures/cli/main.py reads `APP_ENV` from the environment and
  `--format` from `argparse` (both necessarily strings) and parses each
  once into an enum (`Environment(...)`, `OutputFormat(...)`); every
  comparison downstream, in fixtures/cli/export.py, is on the enum.

  PASS if no `high` or `medium` severity Stringly-typed (or Primitive
  obsession) finding targets the reads in `main` / `parse_args` of
  fixtures/cli/main.py. A report with no findings at all passes.
  FAIL if the boundary reads are flagged at high or medium severity.
weight: 1
---

Does not call a string at the boundary stringly-typed when it is parsed
once into a type.
