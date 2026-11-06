---
type: llm
focus: last_message
criteria: |
  The last line of fixtures/bin/import_prices.py ends with
  `# type: ignore[arg-type]  # noqa: E501`: a mypy directive and a flake8
  directive, read by those tools.

  PASS if no finding, at any severity, targets either directive. A report
  with no findings at all passes.
  FAIL if `# type: ignore[arg-type]` or `# noqa: E501` is flagged as
  redundant, verbose, misleading or anything else.
weight: 1
---

Does not judge tool directives as comments: they carry no information for
a reader and cannot be shortened or deleted without changing what the
tools do.
