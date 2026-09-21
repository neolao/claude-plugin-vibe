---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Fixture` (or clearly equivalent
  category name) finding on `TestUserService.setUp` in
  fixtures/test_user_service.py, for using a bare `MagicMock()` as the
  database with nothing about real lookup/persistence semantics configured,
  so the fixture cannot exercise any real storage edge case.
  FAIL if no finding flags the trivial `MagicMock()` fixture.
weight: 1
---

Reports `TestUserService.setUp`'s unconfigured `MagicMock()` database as a
`Fixture` finding.
