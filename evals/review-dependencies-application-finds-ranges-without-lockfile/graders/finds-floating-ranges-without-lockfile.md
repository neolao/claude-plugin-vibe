---
type: llm
focus: last_message
criteria: |
  fixtures/pyproject.toml is an application's manifest: it declares a
  `[project.scripts]` entry point, fixtures/Dockerfile installs the
  checkout itself and runs it, fixtures/README.md deploys it that way and
  nothing publishes it to an index. Its runtime dependencies are
  open-ended ranges (`requests>=2.28`, `click>=8.0`) and no lockfile is
  committed, so each build resolves whatever is current that day.

  PASS if the reported findings include a `Version hygiene` finding on
  `requests>=2.28` or on `click>=8.0` (either is enough) that points at
  the open-ended range or the absent lockfile and asks for pinned
  versions or a committed lockfile.
  FAIL if no `Version hygiene` finding targets either range, or if the
  report treats the manifest as a library whose ranges are the convention.
weight: 1
---

Reports an application's open-ended ranges with no lockfile as a Version
hygiene finding: the library exemption does not apply to a manifest that
is deployed from its checkout.
