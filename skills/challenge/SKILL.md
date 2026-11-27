---
name: challenge
description: Devil's advocate on a structuring decision already settled (architecture, library, strategy, plan) — one read-only sub-agent hunts the blind spot or the unconsidered alternative before the decision is executed, recorded as an ADR or not; not for reversible or minor choices
argument-hint: "[optional: the decision to challenge, or the path of its ADR or plan; empty takes the one under discussion in the conversation]"
version: 1.3.0
model: claude-sonnet-5-5
---

# /vibe:challenge — Devil's Advocate

A decision that has never been attacked has not been tested, only assumed. Challenge a structuring decision that is already settled — an architecture, a library, a strategy, a plan — before it is executed, whether or not it is already recorded in `.vibe/decisions/`. Pairs with `vibe:clarify`, which settles a plan that is still open: `clarify` closes the branches, `challenge` attacks the result. Not for a reversible or minor choice: a pass only pays for itself when the choice is costly to undo.

Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — State the decision

`$ARGUMENTS` if non-empty; otherwise the decision under discussion right before this skill was invoked; if nothing usable is in context, ask ("Which decision do you want challenged?") and wait. An argument that names a file — an ADR under `.vibe/decisions/`, a plan — is read, and its sections give the account below; the decision is the file's, cited by its path. A path that does not exist is nothing usable: ask.

Write the decision neutrally, as an account and not a plea: the option chosen, the context, the known constraints, **the factual reasons for the choice**, and **the alternatives already rejected, each with its motive**. Without the reasons the advocate has nothing to attack and invents some; without the rejected alternatives it re-proposes what was already dismissed. Neither is yours to invent: what the conversation, the argument and the decision's own ADR (when `.vibe/decisions/` holds one) do not give is asked — the reasons for the choice, the alternatives looked at and why they lost — in one question, the same one as "Which decision" when that is asked, and waited for. A user who has none gets `none stated` in the account: that absence is the advocate's to attack, not yours to paper over.

When the decision bears on an existing codebase, the account ends with **the files or directories that ground it** — the code a reason speaks of, the module the choice replaces or extends, the ADR — as absolute paths located by you, never pasted as code: a reason the code contradicts is the blind spot most worth finding, and the advocate can only find it in the code.

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
