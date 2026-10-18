# Principles

## Two framings, then adjust the plan

Nothing can be built without knowing the needs and constraints. Framing happens in two spaces:

| Framing | Space | Question | Where the answer lives |
|---|---|---|---|
| **Frame the need** | Problem space | What must be solved, for whom, under which business constraints? | The request, the backlog item, existing docs |
| **Frame the implementation** | Solution space | Which approach, under which technical constraints? | The code |

The PO is asked only when the answer is in neither place. Each framing looks in its own sources first, and is judged on two things: asking the right questions, and knowing when it can answer alone.

During execution the plan is adjusted, never abandoned. A discovery is answered alone when the code or the docs hold the answer, otherwise it goes to the PO as a decision.

## Verify, then loop

The code is checked by internal agents (findings never reach the PO as a report). A finding is routed by its space:

- problem space → back to framing the need;
- solution space → back to framing the implementation;
- only low-level findings left → deliver.

A finding is a hint that a better solution exists, not a patch to apply blindly.

## Every claim carries its proof

Any claim the PO will not verify themselves (tests pass, feature works, docs match the code) carries a proof — a `file:line`, a command and its result — and a check confirms it.

## Orchestrators delegate

One orchestrator per need keeps the sequence of steps and delegates the work to bricks, so each brick can be evaluated on its own. Progress is tracked by `vibe:tasks`: the orchestrator is judged on following every task without skipping one.

## Shared bricks

Framing, review agents, the findings classifier, the claim check and the clarity rewrite are shared across orchestrators. What differs is what each orchestrator does with their result.
