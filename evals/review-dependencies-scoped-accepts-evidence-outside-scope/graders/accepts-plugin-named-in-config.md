---
type: llm
focus: last_message
criteria: |
  `pytest-cov` is declared in the `dev` extra of fixtures/pyproject.toml.
  No file imports it: it is a pytest plugin, loaded by pytest and driven by
  the `--cov` options in `[tool.pytest.ini_options] addopts` of the same
  manifest.

  PASS if no `high` or `medium` severity `Unused` finding targets
  `pytest-cov`. A report whose only finding says the audit tool could not
  run passes.
  FAIL if `pytest-cov` is flagged as unused at high or medium severity.
weight: 1
---

Does not call a plugin unused because nothing imports it: the config that
names it is its use.
