---
date: 2026-02-03
status: accepted
---
# The mobile client keeps its own copy of the ticket status list
**Context:** The backend adds a status every few months; the mobile client ships through the app stores on a release cycle of its own, and users keep old versions for weeks. A mobile build cannot depend on the backend's list of the day.
**Decision:** `mobile/Statuses.kt` holds its own list of statuses and maps any status it does not know to `UNKNOWN`, displayed as "Other". The backend's `tickets/status.py` is the reference; the mobile copy is updated when a release of the client is planned, never in the same change as the backend.
**Reason:** A shared definition would couple two release cycles that are independent by nature; a runtime fetch of the list was rejected because the client must render tickets offline.
**Rejected alternatives:** Generating the Kotlin file from the Python list at backend build time — the artifact would still have to wait for a client release, and the generator added a toolchain to the backend for nothing.
