---
date: 2026-07-02
status: accepted
---
# The public API says `customer`; `buyer` is retired
**Context:** The mobile app shipped the rename in its spring release: it reads `customer_id` and calls `/customers/<id>/orders`. Decision 001 kept `buyer` in the API only until then.
**Decision:** Every path and payload says customer. `buyer` appears nowhere in the code. This supersedes decision 001.
**Reason:** One word for one concept, in the API as in the domain, now that nothing depends on the old one.
**Rejected alternatives:** Keeping the old routes as aliases — no client calls them any more.
