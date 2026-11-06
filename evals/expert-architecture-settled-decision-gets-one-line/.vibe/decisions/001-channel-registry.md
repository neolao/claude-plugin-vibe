---
date: 2026-03-14
status: accepted
---
# A delivery channel is one adapter module registered by name, never a branch in the router
**Context:** The second channel (push) was first added as an `elif` in `core/notification_router.py` next to email, with the provider client imported into core; the router changed for every channel and could not be tested without both SDKs installed.
**Decision:** `core/notification_router.py` holds a registry keyed by channel name and dispatches on `message.channel`; it never names a channel. Each channel is one module under `adapters/notify/` exposing `send(message)` and registering itself with `@register("<name>")`; `adapters/notify/__init__.py` imports every channel module so registration runs at startup. Adding a channel adds one module and one import line and touches nothing in `core/`.
**Reason:** The router stays closed to new channels, each adapter is testable on its own, and no provider SDK enters core.
**Rejected alternatives:** A `Channel` base class with one subclass per provider — more ceremony than a function and a decorator for a module with one entry point. A `match` on the channel name in the router — the shape that caused the problem.
