---
date: 2026-03-14
status: accepted
---
# Provider SDKs live in adapters behind a port owned by core
**Context:** The first version called the mail provider's SDK from the service that builds the notification; the service could not be tested without the provider's credentials, and changing provider meant editing business code.
**Decision:** `core/ports.py` owns the `Notifier` port. Every provider SDK is wrapped in a class under `adapters/notify/` that implements it. `core/` imports nothing from `adapters/`; `app.py` wires the concrete notifiers into the service.
**Reason:** The service is testable with fake notifiers, and a provider is replaceable without touching `core/`.
**Rejected alternatives:** Mocking the SDK in the tests — kept the dependency on the provider's types in business code.
