---
type: llm
focus: last_message
criteria: |
  The seven existing services carry their database and Redis passwords in
  the images they ship from; the brief adds an eighth service and changes
  nothing else. Moving the existing passwords out of seven images is a
  separate change with its own rollout.

  PASS if no REQUIREMENTS entry makes moving the existing services'
  passwords out of their images, rebuilding or re-deploying the seven
  services, or rotating their passwords a non-negotiable of this change.
  The gap may be named in RISKS, as a later migration, or as advice for a
  future change: that passes.
  FAIL if REQUIREMENTS demands that the existing seven services' secrets be
  moved out of their images, rotated or re-deployed as part of this change.
weight: 1
---

Keeps the seven existing services out of this change's REQUIREMENTS: the
registry-readable passwords are a named follow-up, not a condition of
shipping the eighth service.
