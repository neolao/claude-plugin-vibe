---
type: llm
focus: last_message
criteria: |
  The fixtures each superficially resemble a robustness defect but are
  already handled correctly:
  - `payment_gateway.py`'s `charge_card` catches a specific
    `GatewayTimeoutError` (not a broad `Exception`), logs it with the order
    id and amount, and re-raises (`raise`) instead of continuing — a failed
    charge stops the flow, it never reaches `return {"status": "paid"}`.
  - `webhook_dispatcher.py`'s `complete_order` creates a task like an
    unawaited fire-and-forget call would, but its docstring explicitly marks
    it as intentional fire-and-forget, and `notify_partner` itself catches
    and logs its own failure with the order id — nothing is silently lost.
  - `report_client.py`'s `fetch_report` looks like a retry loop, but it caps
    attempts at `max_attempts`, sleeps with exponential backoff between
    tries, passes `timeout=10` to `requests.get`, and raises a final error
    that names both the url and the attempt count.
  - `export_writer.py`'s `export_orders` opens a file like a leak risk would,
    but uses a `with` block, so the file is guaranteed to close even if a
    write raises. Its `load_export_template` re-raises inside an `except`
    like a lost-context bug would, but uses `raise ... from e` (preserving
    the original cause) and includes `path` in the new message.

  PASS if the response reports no `high` or `medium` severity Swallowed
  error, Async, Timeout/limit, Resource, or Lost context finding on this
  code — either no findings at all, or only `low` severity style notes
  unrelated to these already-handled patterns.
  FAIL if it flags `charge_card`'s specific catch-and-reraise as swallowing
  the error, `complete_order`'s explicitly-marked fire-and-forget task as a
  silent-failure risk, `fetch_report`'s bounded/backed-off/timed retry as
  missing a timeout or cap, `export_orders`'s `with`-guarded write as a
  resource leak, or `load_export_template`'s `raise ... from e` (with the
  path included) as losing context.
weight: 2
---

Does not invent robustness findings on code that already handles each
failure mode correctly.
