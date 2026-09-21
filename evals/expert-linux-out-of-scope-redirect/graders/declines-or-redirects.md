---
type: llm
focus: last_message
criteria: |
  PASS if the reply is short and either says it has no real concern in its
  domain (shell scripting / POSIX portability / system-level integration), or
  explicitly redirects the brief to `expert-cli-dx` (CLI flags/help/output),
  without inventing detailed REQUIREMENTS/RISKS/TEST SCENARIOS about flag
  design, `--help` output, `--json` mode, or exit codes as if those were its
  own domain.
  FAIL if the reply confidently produces detailed, domain-specific
  REQUIREMENTS/RISKS/TEST SCENARIOS about flag naming, help text, or CLI exit
  codes as though the Linux/system expert owned that advice.
weight: 2
---

Declines or redirects instead of fabricating CLI-UX advice outside its
Linux/system domain.
