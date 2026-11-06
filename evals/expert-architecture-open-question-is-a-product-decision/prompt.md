---
name: expert-architecture-open-question-is-a-product-decision
description: >-
  Recall of the open-question rule of expert-architecture: whether a
  second promotion is a second branch in the pricing function or the start
  of a promotion-rule structure depends on what marketing will ask for
  next and on whether promotions combine — facts the brief leaves open and
  only the product can settle. The expert must ask that as an open
  question phrased for a non-technical Product Owner, saying which option
  each answer picks, and must not ask the caller any technical detail or to
  choose between the named options.
tags: [expert-architecture, recall, open-questions]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:expert-architecture` sub-agent (Agent tool, `subagent_type: "vibe:expert-architecture"`) with this brief, the plan notes and the consultation request below. The code is in `fixtures/` of this case directory; the project has no `.vibe/`.

Brief:

```
Our shop's pricing applies a percentage coupon to the cart. We're adding a
"buy 2, get 1 free" promotion on a set of products. Marketing says they
have more promotion ideas for next year but nothing is decided, and nobody
has said yet whether the coupon and the promotion can apply to the same
cart. How should we shape this?
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
