---
type: regex
target: last_message
pattern: "expert-ops"
flags: i
weight: 2
---

The redirect names `expert-ops` by its id, not a generic "ops/infra
expert" nor `expert-linux`: the invoking skill never gives an expert the
roster, so the name has to come from the scope sentence, which routes how a
daemon is configured, deployed, observed and kept running there.
