---
type: llm
focus: last_message
criteria: |
  The fixture's `.vibe/decisions/001-channel-registry.md` (status accepted)
  decides exactly the brief's question: a channel is one module under
  `adapters/notify/` that registers its `send` function with
  `@register("<name>")` in `core/notification_router.py`, and the router
  dispatches on the channel name; `email.py` and `push.py` follow it. The
  expert's own rule: a brief the repo already prescribes the form of gets a
  one-line reply naming the decision or the idiom.

  PASS if the reply says the choice is already settled and points at that
  decision (by number, title or file) or at the registry in
  `core/notification_router.py` (`CHANNELS`, `@register`) as the form the
  SMS channel follows — naming both is ideal, either one passes.
  FAIL if the reply names neither the decision nor the registry, or treats
  where the SMS code lives and how it is picked as an open choice.
weight: 2
---

Names the recorded decision (or the registry it prescribes) as what already
settles the brief, instead of treating the choice as open.
