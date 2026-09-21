---
type: llm
focus: last_message
criteria: |
  PASS if the reply is short and either says it has no real concern in its
  domain (CLI flags/help/output/exit codes), or explicitly redirects the brief
  to `expert-linux` (shell scripting / system integration), without inventing
  detailed REQUIREMENTS/RISKS/TEST SCENARIOS about systemd units, dedicated
  system users, or GNU vs BSD coreutils as if those were its own domain.
  FAIL if the reply confidently produces detailed, domain-specific
  REQUIREMENTS/RISKS/TEST SCENARIOS about the system-user creation, systemd
  unit, or cross-OS shell portability as though CLI-DX owned that advice.
weight: 2
---

Declines or redirects instead of fabricating system-integration advice
outside its CLI/DX domain.
