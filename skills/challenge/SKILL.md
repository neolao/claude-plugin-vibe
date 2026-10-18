---
name: challenge
description: Devil's advocate on a structuring decision already settled (architecture, library, strategy, plan) — one read-only sub-agent hunts the blind spot or the unconsidered alternative before the decision is executed or recorded as an ADR; not for reversible or minor choices
argument-hint: "[optional: the decision to challenge; empty takes the one under discussion in the conversation]"
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:challenge — Devil's Advocate

A decision that has never been attacked has not been tested, only assumed. Challenge a structuring decision that is already settled — an architecture, a library, a strategy, a plan — before it is executed or recorded in `.vibe/decisions/`. Pairs with `vibe:clarify`, which settles a plan that is still open: `clarify` closes the branches, `challenge` attacks the result. Not for a reversible or minor choice: a pass only pays for itself when the choice is costly to undo.

Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — State the decision

`$ARGUMENTS` if non-empty; otherwise the decision under discussion right before this skill was invoked; if nothing usable is in context, ask ("Which decision do you want challenged?") and wait.

Write the decision neutrally, as an account and not a plea: the option chosen, the context, the known constraints, **the factual reasons for the choice**, and **the alternatives already rejected, each with its motive**. Without the reasons the advocate has nothing to attack and invents some; without the rejected alternatives it re-proposes what was already dismissed.

## Step 2 — Launch the advocate

Launch **one** agent (Agent tool, `subagent_type: "general-purpose"`, `model: "opus"` — the tool takes an alias, not a full model id — `run_in_background: false`, so the analysis comes back in this turn). Its prompt opens with this sentence verbatim: "Read-only: you modify no file and produce only an analysis. Do it yourself: invoke no skill and launch no agent." Then the full content of `references/advocate.md` next to this file (`${CLAUDE_PLUGIN_ROOT}/skills/challenge/references/advocate.md`), then the decision as written in Step 1.

One pass: this is not an iterative quality gate, there is no retry loop.

## Step 3 — Report

Report **every** objection the advocate returned, one entry per number in its own numbering (`O1`, `O2`…) — never merge two, never fold one into a summary. Under each, give your own opinion: kept or dismissed, and why. The user decides, not you: you authored the decision under attack, so filtering what counts as "real" would reproduce the very bias this skill fights. A kept objection may change the decision or become a rejected alternative in its ADR under `.vibe/decisions/`.

End with:

```
---
⚔️ Challenge — [Blind spot found: <short summary> | Nothing found]
---
```

`Nothing found` is allowed only when the advocate concluded so itself.
