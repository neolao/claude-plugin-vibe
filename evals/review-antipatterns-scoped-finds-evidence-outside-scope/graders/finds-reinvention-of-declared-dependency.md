---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Wheel reinvention` (or clearly
  equivalent category name) finding on `parse_version` / `client_supported`
  in fixtures/orders/version_check.py that points to the `semver` package
  (declared in fixtures/requirements.txt) as the replacement for the
  hand-rolled version comparison.
  FAIL if no finding flags the hand-rolled version comparison, or if the
  finding proposes only a library the project does not declare (for example
  `packaging`) without mentioning `semver`.
weight: 1
---

Reports the hand-rolled version comparison in fixtures/orders/version_check.py
as Wheel reinvention of the `semver` dependency the project already declares.
Naming `semver` rather than a library the project does not have shows the
manifest outside the scope was read, not guessed at.
