---
name: clarify
description: Interview the user relentlessly, round by round, over a plan, idea, or decision until every open branch is settled — finds facts itself, never guesses what only the user can decide
argument-hint: "[optional: subject to clarify — plan, idea, or decision; empty infers it from the current conversation]"
---

# /vibe:clarify — Relentless Interview

Stress-test a plan, idea, or decision by mapping it as a **design tree** — every decision branches into the decisions that hang off it — and interviewing the user round by round until the tree is settled. Runs standalone, or invoked by `vibe:backlog`, `vibe:init`, or `vibe:workspace-init` when their input is too thin to act on without inventing answers.

Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — Subject

`$ARGUMENTS` if non-empty; otherwise the plan, idea, or description under discussion right before this skill was invoked; if nothing usable is in context, ask ("What plan, idea, or decision do you want me to grill you on?") and wait. State the subject back in one line before starting.

## Step 2 — Design tree

As working notes, never shown: the subject at the root, every decision needed to fully specify it, each branching into the decisions that depend on its answer. It grows and reshapes as answers arrive.

## Step 3 — Rounds

The **frontier** is every open decision whose prerequisites are settled — askable now without guessing an unheard answer; a question depending on another open one waits for a later round.

**Fact-finding is never the user's job.** Anything answerable by looking (codebase, backlog, `.vibe/`, configs, manifests) is found instead — dispatch a sub-agent (Agent tool, `general-purpose`) without blocking the round on it; only the questions that depend on that fact wait.

Ask the whole remaining frontier in one round, numbered, each with your recommended answer:

```
❓ **Q1** - **<question title>**: <question body, possibly with choices>

➡️ <your recommended answer>

---

❓ **Q2** - ...
```

Then stop and wait for the user's answers before asking the next round or acting on anything. Each answer settles a decision and may unblock others; a sub-agent's finding is folded in the same way. Recompute the frontier and repeat.

## Step 4 — End

When the frontier is empty, summarize the shared understanding and ask the user to confirm it before treating it as final or handing it to a caller. If the user stops early (declines to continue, says the rest does not matter), respect that and report what was settled, flagging the rest as open.

## Step 5 — Report

One report for both audiences — the human, and a caller skill that parses the literal headings:

```
CLARIFY-RESULT: settled
### Synthesis
[2–5 plain sentences, in the conversation's language, folding every settled decision into one description of the subject — written to directly replace the caller's original input]

### Decisions made
- **[question title]**: [answer reached]
```

Ended early → `CLARIFY-RESULT: partial — [what is still open]` with the content actually reached. Nothing settled at all → `CLARIFY-RESULT: abandoned`, no sections; the caller falls back to its original input.
