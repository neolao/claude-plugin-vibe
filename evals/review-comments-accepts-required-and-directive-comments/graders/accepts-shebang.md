---
type: llm
focus: last_message
criteria: |
  fixtures/bin/import_prices.py opens with `#!/usr/bin/env python3`, a
  shebang the shell reads, not a comment for a person.

  PASS if no finding, at any severity, targets that first line. A report
  with no findings at all passes.
  FAIL if the shebang is flagged as redundant, verbose, misleading or
  anything else.
weight: 1
---

Does not judge a shebang as a comment: the sed mask would strip it like any
`#` line, but it is read by the shell.
