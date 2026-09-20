---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `O` (or clearly equivalent OCP)
  finding on the `if`/`elif`/`else` channel dispatch in
  `NotificationSender.send`, noting that adding a new channel requires
  editing this method rather than adding a new case elsewhere.
  FAIL if no finding flags this dispatch chain as an OCP violation.
weight: 1
---

Reports the channel `if`/`elif` chain in `NotificationSender.send` as an `O`
finding.
