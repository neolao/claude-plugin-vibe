---
date: 2026-08-03
status: accepted
---
# The entry point hands the handler table to `Dispatcher`; the import-time registry is retired
**Context:** Decision 001 filled a module-level `HANDLERS` dict at import time. The test suite and the admin console both mutate that dict (to swap a handler, to disable one), and two incidents came from a handler registered twice under one name by an import order nobody controlled.
**Decision:** `shop/dispatch.py` exposes `Dispatcher(handlers)`, built once by `main.py` from an explicit dict of the handler functions. Handler modules export their `handle` function and register nothing. `shop/handlers/__init__.py` holds no table. This supersedes decision 001.
**Reason:** The table is built in one place, read-only afterwards, and every test or console gets its own `Dispatcher` instead of editing shared state.
**Rejected alternatives:** Keeping the registry and locking it after startup — the writers (tests, admin) would still need their own copy, which the constructor gives them for free.
