---
date: 2026-03-12
status: accepted
---
# Order handlers register themselves in the module-level `HANDLERS` dict at import time
**Context:** Each order event (billing, shipping, and the ones the next quarters add) is handled by its own module under `shop/handlers/`. The dispatcher needs the full table of handlers, and the project has no dependency-injection container.
**Decision:** `shop/handlers/__init__.py` holds a module-level `HANDLERS` dict and a `register(name, handler)` function. Every handler module calls `register` at import time; `shop/dispatch.py` imports the handler modules for that side effect and reads `HANDLERS`. Adding a handler is one new module and nothing else.
**Reason:** Django already discovers apps and models by import; a registry filled at import follows the same convention, and the table is complete before the first request because the dispatcher imports every handler module itself.
**Rejected alternatives:** A `Dispatcher(handlers)` constructor fed by the entry point — every new handler would have to be added to the entry point as well, the exact double edit this decision removes. A plugin framework — more than a dict of five callables needs.
