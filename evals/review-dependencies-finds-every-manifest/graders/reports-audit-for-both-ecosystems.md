---
type: llm
focus: last_message
criteria: |
  The repository holds two manifests of two ecosystems:
  fixtures/api/pyproject.toml (Python, audited with pip-audit) and
  fixtures/web/package.json with its package-lock.json (Node, audited with
  npm audit). Neither audit can complete in this environment (pip-audit
  is not installed, the registry is unreachable).

  PASS if the report says that the audit could not run for BOTH manifests:
  either one `Vulnerability` finding naming both tools or both manifests,
  or one such finding per manifest. Each must say the audit could not run
  and why, never that the vulnerability check came back clean.
  FAIL if only one ecosystem's audit is reported (the other manifest is
  never mentioned as audited or unaudited), or if the report states or
  implies that either manifest's vulnerability check came back clean.
weight: 1
---

Reports an audit that could not run for each ecosystem present, instead
of auditing the first stack found and keeping silent on the other.
