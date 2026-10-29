---
type: regex
target: trace
pattern: "(?=[\\s\\S]*incr returns\\.implementation(?![.\\w]))(?=[\\s\\S]*incr rounds(?![.\\w]))(?=[\\s\\S]*incr fixes(?![.\\w]))"
weight: 1
---

The return to the implementation framing, the new round and the fix are each counted.
