---
type: llm
focus: last_message
criteria: |
  `pip-audit` is not installed in the environment, and no lockfile is
  committed, so no vulnerability audit can run on fixtures/.
  PASS if the reported findings include a `Vulnerability` finding saying
  that the audit tool (`pip-audit` or equivalent) is missing or could not
  run, so the project's vulnerabilities are not checked automatically.
  FAIL if no finding reports that the audit could not run, or if the
  report states or implies the vulnerability check came back clean.
weight: 1
---

Reports the audit that could not run as a finding, instead of treating the
category as clean.
