---
name: clarify
description: Interview the user relentlessly, round by round, over a plan, idea, or decision until every open branch is settled — finds facts itself, never guesses what only the user can decide
argument-hint: "[optional: subject to clarify — plan, idea, or decision; empty infers it from the current conversation]"
---

# /vibe:clarify — Relentless Interview

Stress-tests a plan, an idea, or a decision by mapping it as a **design tree** — every decision branches into the decisions that hang off it — and interviewing the user round by round until the whole tree is settled. Runs standalone (`/vibe:clarify`), or invoked by another skill (`vibe:backlog`, `vibe:init`, `vibe:workspace-init`) when what it has to work with is too thin to proceed safely without silently inventing answers. Either way it ends with a summary the caller — human or skill — can act on (see Step 5).

## Step 1 — Determine the subject

- `$ARGUMENTS` non-empty → that is the subject, verbatim.
- `$ARGUMENTS` empty → infer the subject from the current conversation: the plan, idea, or description under discussion right before this skill was invoked. If nothing usable is found in context either: ask the user directly — in the language the conversation is being conducted in, e.g. "What plan, idea, or decision do you want me to grill you on?" in English — and wait for their answer before continuing.

State the subject back to the user in one line before starting, so they know what's being grilled — same language rule.

**Language.** Every message this skill writes to the user — this one, the rounds in Step 3, the confirmation in Step 4 — is written in the language the current conversation is being conducted in. Never hardcode a specific language: this skill runs across arbitrary projects and conversations. (This file's own instructions, like every other skill in this plugin, are authored in English — only the live dialogue with the user adapts.)

## Step 2 — Map the design tree

Before asking anything, sketch the design tree for the subject as your own working notes (never shown verbatim to the user): the subject at the root, and every decision that has to be made to fully specify it, branching into the decisions that depend on its answer. This is a starting sketch, not a final map — it grows and reshapes as rounds answer questions and expose new branches (Step 3).

## Step 3 — Work the frontier, one round at a time

The **frontier** is every open decision in the tree whose prerequisites are already settled — the questions that can be asked *now* without guessing at an answer not yet heard. A question whose answer depends on another still-open question belongs to a *later* round, not this one.

**Fact-finding is never the user's job.** Before asking the frontier, check whether any of it can instead be answered by looking — the codebase, existing backlog items, `.vibe/`, config files, manifests, whatever is reachable. For anything that needs that kind of lookup: dispatch a sub-agent (Agent tool, `subagent_type: "general-purpose"`) to find it, and don't block the round on it — only the questions that depend on that specific fact wait for it; ask the rest of the frontier now. Never ask the user something you could find yourself.

Ask the whole remaining frontier in one round, numbered, each with your own recommended answer, written in the conversation's language:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body>

➡️ <your recommended answer>
```

Then stop and wait — do not ask the next round, do not act on any answer, until the user has responded to this one.

Each answer reshapes the tree: it settles a decision, which may unblock questions that depended on it. Recompute the frontier from the updated tree and repeat this step for the next round. If a dispatched sub-agent reports back before the next round starts, fold its finding into the tree the same way — it may itself unblock more of the frontier.

## Step 4 — End condition

The session ends when the frontier is empty: every branch of the tree has been visited, nothing left silently assumed. At that point, summarize the shared understanding reached and ask the user to confirm it before treating it as final — do not act on it, and do not hand it to a caller skill, until they confirm.

If the user stops the session early instead (declines to continue, says the remaining branches don't matter, or explicitly asks to move on): respect that. Go to Step 5 and report what was actually settled, flagging the rest as still open rather than inventing answers for it.

## Step 5 — Report

Two audiences read this report identically — a human who typed `/vibe:clarify`, and a skill that invoked it (`vibe:backlog`, `vibe:init`, `vibe:workspace-init`) and needs to keep going with what it says. Write it once, in this shape:

```
CLARIFY-RESULT: settled
### Synthesis
[2–5 plain sentences, in the conversation's language, folding every settled decision into a single coherent description of the subject — written so it can directly replace the caller's original, under-specified input]

### Decisions made
- **[question title]**: [answer reached]
- **[question title]**: [answer reached]
```

The section headings (`### Synthesis`, `### Decisions made`) stay as literal markers — a caller skill (`vibe:backlog`, `vibe:init`, `vibe:workspace-init`) parses them by this exact text regardless of conversation language, so keep them fixed.

If the session ended early (Step 4, user stopped before the frontier was empty): use `CLARIFY-RESULT: partial — [what's still open, one short phrase]` instead of `settled`, and still include whatever `### Synthesis` / `### Decisions made` content was actually reached — a caller skill can use a partial synthesis, it just should not treat it as exhaustive.

If nothing was settled at all (the user stopped before round 1 produced any answer): use `CLARIFY-RESULT: abandoned` and omit both sections — a caller skill falls back to its own original input in that case.
