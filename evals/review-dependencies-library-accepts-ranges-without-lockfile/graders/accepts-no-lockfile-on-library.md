---
type: llm
focus: last_message
criteria: |
  fixtures/ contains no lockfile (no requirements.txt, poetry.lock or
  uv.lock). The manifest is a library published to PyPI (see
  fixtures/README.md and the PyPI homepage in fixtures/pyproject.toml): a
  library commits no lockfile on purpose, since its consumers resolve the
  versions.

  PASS if no `high` or `medium` severity `Version hygiene` finding says the
  project lacks a lockfile or that its dependencies are unpinned because
  of it. Only a finding block (`PACKAGE:` ... `CATEGORY:` ...
  `SEVERITY:`) counts. A `Vulnerability` finding that says the audit could
  not run, even one that gives the absent lockfile or the missing
  pip-audit as the reason, is not a Version hygiene finding and passes.
  FAIL if a `Version hygiene` finding at high or medium severity asks the
  library to commit a lockfile.
weight: 1
---

Does not ask a library to commit a lockfile.
