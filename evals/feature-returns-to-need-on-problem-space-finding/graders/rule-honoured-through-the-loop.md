---
type: llm
focus: trace
criteria: |
  The brief never mentions `null` readings. The rule lives in
  `.vibe/decisions/001-missing-readings-are-skipped.md`. The workflow has two
  legitimate ways to honour it, and this grader accepts either:

  (a) **Caught at framing.** The `vibe:clarify` run in `mode: need` settled a
      decision about `null` / missing readings being skipped, citing the
      decision file as its source (`(source: .vibe/decisions/001…)` or the
      file quoted in its report).

  (b) **Caught at review.** The need framing missed it; a review agent
      (typically `review-architecture`, active because `.vibe/` exists) or
      `requirements-reviewer` raised it; `review-classifier` put it in the
      `need` space at high or medium; the run then went back to the need
      framing — visible as a second `vibe:clarify … mode: need` invocation
      mentioning "Round 2", a `report.sh … incr returns.need` call, or
      `Round 2 — ` tasks created through `vibe:tasks` — and the code was
      changed afterwards.

  PASS on (a) or (b).
  FAIL if the trace shows neither: the rule reached the code with no source
  cited and no review round, or the code never honoured it, or a need-space
  finding was downgraded or dropped without a documented reason.
weight: 3
---

The rule was honoured because the loop found it, not by luck: a sourced
framing decision, or a classified finding that sent the run back.
