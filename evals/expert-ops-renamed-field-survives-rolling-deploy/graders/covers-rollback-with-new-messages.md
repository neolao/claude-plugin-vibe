---
type: llm
focus: last_message
criteria: |
  PASS if the reply states a rollback path and addresses that messages in the
  new format may already sit on the bus when the rollback happens (the bus
  keeps them seven days): for example the rolled-back version and every reader
  must still understand messages carrying `carrier_code`, or old readers
  ignore the unknown field, or the old field keeps being published so a
  rollback loses nothing.
  FAIL if there is no rollback path, or the rollback is "redeploy the previous
  version" with no word on messages already published in the new format.
weight: 2
---

States a rollback path that holds for new-format messages already on the bus.
