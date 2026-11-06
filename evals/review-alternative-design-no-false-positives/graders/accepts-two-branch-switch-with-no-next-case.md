---
type: llm
focus: last_message
criteria: |
  `send` in fixtures/notifications/sender.py switches on two channels
  (`email`, `sms`). It is the only switch on the channel in the
  repository, no other file branches on it, and nothing in the repository
  announces a third channel.

  PASS if no `high` or `medium` severity finding proposes a Strategy
  registry, a channel table, a Chain of Responsibility, an adapter per
  channel or any other named design for `send`. A report with no findings
  at all passes.
  FAIL if such a design is proposed for `send` at high or medium severity
  on the ground that a third channel would be cheaper to add.
weight: 1
---

Does not score extensibility on a variant nothing shows is coming: a lone
two-branch switch gets no registry.
