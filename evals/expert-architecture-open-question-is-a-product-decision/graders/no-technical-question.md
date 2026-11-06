---
type: llm
focus: last_message
criteria: |
  `/vibe:feature` puts OPEN QUESTIONS straight to a non-technical Product
  Owner, in plain words. The expert's rule: a technical fact it could not
  establish is never a question — it is read from the code or stated as an
  assumption — and a technical default it can pick itself is not asked.

  PASS if no OPEN QUESTIONS entry asks the caller a technical detail or to
  arbitrate between the expert's options: no question about a pattern or
  structure (strategy, specification, rules engine, class versus function),
  about the code (which file, whether `total()` is on a hot path, how often
  it is called), about a framework or library, and no "do you prefer
  option A or option B". Rounding, tax or currency questions are product
  questions and pass, and so do questions about how a promotion behaves
  (whether products mix, which unit is free, whether the offer repeats) or
  about what the customer sees on the cart page. Judge the question
  sentence itself: the per-answer explanations beneath it may name the
  option each answer picks, and doing so does not make the question
  technical.
  FAIL if the question sentence of an OPEN QUESTIONS entry itself asks such
  a technical detail, makes a pattern or a code identifier the thing to
  decide, or asks the Product Owner to choose between the named options.
  A question about what the business will do (promotions that may combine,
  further promotions coming, what is shown to customers) passes even when
  the answer lines beneath it say which option or which file that answer
  leads to: the agent is required to say so.
weight: 2
---

Keeps technical facts and the choice between its own options out of the
questions to the Product Owner.
