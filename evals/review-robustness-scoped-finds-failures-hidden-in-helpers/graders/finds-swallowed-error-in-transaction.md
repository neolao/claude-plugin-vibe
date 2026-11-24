---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Swallowed error` (or clearly
  equivalent category name) finding on `charge_order`
  (fixtures/billing/charge.py): it runs the status update and
  `gateway.capture` inside `transaction(conn)`, and `transaction`
  (fixtures/db/tx.py) catches `Exception`, rolls back and logs without
  re-raising, so a failed capture leaves the `with` block normally and
  `charge_order` still returns `charged: True` to the checkout flow. The
  finding must say that the failure does not reach `charge_order`'s caller
  (swallowed, not re-raised, or reported as charged anyway); a finding that
  only says the transaction logs the error does not count.
  FAIL if no finding flags this.
weight: 1
---

Reports the capture failure that the transaction helper outside the scope
swallows, so checkout reports the order as charged.
