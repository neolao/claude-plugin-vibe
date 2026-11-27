---
date: 2026-10-02
status: accepted
---
# Projects are stored in one SQLite file per workspace
**Context:** The desktop app keeps the user's projects on their machine: a project holds up to a few hundred thousand rows (layers, shapes, revisions) and is edited offline. A save must land whole or not at all.
**Decision:** One SQLite database file per workspace, opened by `app/store.py`; a project is a set of rows in it, saved in one transaction.
**Reason:** Single user, offline first, ships inside the one binary with nothing to install; a transaction covers a whole save; the prototype's largest project loads in under a second.
**Rejected alternatives:** (1) PostgreSQL — the installer would have to bundle and supervise a server process. (2) One JSON file per project — no transactions, and a project above a few thousand records took seconds to save in the prototype. (3) A cloud store — the app must work offline on a plane.
