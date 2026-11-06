---
name: expert-architecture-technical-fact-is-assumed-not-asked
description: >-
  Precision side of the open-question rule: the brief settles every
  product decision (exactly two promotions, they never stack, nothing else
  this year) and leaves only a technical unknown — how hot the pricing
  code is — that the fixture's callers answer. The expert must ask no
  open question at all, and settle the call frequency by reading the
  callers or by stating an explicit assumption with the option that holds
  if it is wrong, never by asking.
tags: [expert-architecture, precision, open-questions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-architecture` sub-agent (Agent tool, `subagent_type: "vibe:expert-architecture"`) with this brief, the plan notes and the consultation request below. The code is in `fixtures/` of this case directory; the project has no `.vibe/`.

Brief:

```
Our shop's pricing applies a percentage coupon to the cart. We're adding a
"buy 2, get 1 free" promotion on a set of products. Product has decided:
these two promotions and nothing else this year, and they never stack — the
coupon applies to what remains after the free items. The offer counts units
of the same product only (3 of one product, 1 free), and the cart page keeps
showing just the final total. The set of promoted products is fixed and
only changes with a release. We're not sure how
hot the pricing code is. How should we shape this?
```

Plan notes (send after the brief):

```
The code is in `fixtures/` of the working directory: package `shop/`
(`cart.py`, `pricing.py`, `checkout.py`, `cart_view.py`). The project has
no `.vibe/`.
```

Consultation request (send verbatim, appended to the notes):

```
Reply, in place of the usual three lists, with: BASELINE: (the obvious approach a competent developer writes, named, against the real files, with its cost and weak criteria), ALTERNATIVES: (up to two named patterns, each scored against the baseline on an explicit grid with a BETTER / TIE / WORSE verdict and the count of criteria won and lost), RECOMMENDATION: (one option, justified by the constraints). Add OPEN QUESTIONS: (≤3) only when a real product decision in your domain is genuinely undetermined by the brief — not a technical detail you can decide yourself; phrase each for a non-technical Product Owner.
```

Report the sub-agent's reply back verbatim, and add no commentary of your own: the reply itself is what is being evaluated.
