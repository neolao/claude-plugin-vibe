---
name: findings-classifier-drops-merges-and-routes
description: findings-classifier must drop the false positive (None is handled at pricing.py:15), merge the two findings on the same boundary bug, keep that bug as high · implementation, and route the missing VIP tier to the need space; output in the three-section contract
tags: [findings-classifier, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:findings-classifier` sub-agent (Agent tool, `subagent_type: "vibe:findings-classifier"`) with exactly this prompt:

```
Classify the findings below. Working directory: the current directory; the deliverable is the code in `fixtures/`. Type of deliverable: code.

REQUEST (brief approved by the Product Owner):
"Returning customers get a loyalty discount: 10% once they have spent 500 or more over the last year. VIP customers (flag `vip` on the order) always get 20%, whatever they spent."

RAW FINDINGS:
1. review-correctness — fixtures/pricing.py:8 — `spent_last_year > LOYALTY_THRESHOLD` excludes the threshold; the docstring and the brief say it is included. A customer who spent exactly 500 gets no discount.
2. review-tests — fixtures/test_pricing.py:7 — no test exercises the boundary value 500; the off-by-one at pricing.py:8 goes undetected.
3. review-robustness — fixtures/pricing.py:19 — `price_order` passes `order["total"]` straight to `apply_discount`, which multiplies it; a `None` total raises a TypeError.
4. review-correctness — fixtures/pricing.py:19 — the brief grants VIP customers 20% whatever they spent; nothing in the module reads a `vip` flag or returns 0.20.
```

Once the sub-agent returns, report its output back verbatim.
