---
name: clarify
description: Interview the user round by round over a plan, idea, or decision until every open branch is settled — finds facts itself, never guesses what only the user can decide. Two modes for the build workflow, `need` (what to solve, for whom) then `implementation` (how), each looking in its own sources before asking. Invoked by other vibe skills, never directly by users.
argument-hint: "[mode: need | mode: implementation] [subject to clarify — plan, idea, or decision; empty infers it from the current conversation]"
user-invocable: false
version: 1.2.0
model: claude-sonnet-5-5
---

# vibe:clarify — Relentless Interview

Stress-test a plan, idea, or decision by mapping it as a **design tree** — every decision branches into the decisions that hang off it — and interviewing the user round by round until the tree is settled. Invoked by `vibe:backlog`, `vibe:init`, or `vibe:workspace-init` when their input is too thin to act on without inventing answers, and twice by the build workflow, once per space (see "Modes").

Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — Subject

`$ARGUMENTS` if non-empty; otherwise the plan, idea, or description under discussion right before this skill was invoked; if nothing usable is in context, ask ("What plan, idea, or decision do you want me to grill you on?") and wait. State the subject back in one line before starting.

## Step 2 — Design tree

As working notes, never shown: the subject at the root, every decision needed to fully specify it, each branching into the decisions that depend on its answer. It grows and reshapes as answers arrive. An option the user discards stays in the tree as `[Eliminated]` with the reason — a trace, nothing left to settle.

**Priorities.** Every settled decision carries one: `🔒 MUST` (non-negotiable) | `⚖️ SHOULD` (strong default, sacrificed only to a MUST) | `✨ NICE` (best effort, first sacrificed). The icons are shape-coded (lock, scales, sparkle), never a red/yellow/green scheme, so colour-blind users can tell them apart. Infer it from the user's wording ("absolutely", "mandatory" → MUST; "should", "preferably" → SHOULD; "if possible", "bonus" → NICE), or ask it explicitly in the same round when the wording does not settle it — never default it. A decision you introduced yourself (where code lives, a mechanism, a risk) has no priority in the user's words: its priority is a question of the first round even when the decision itself waits on another answer (one question may group several proposed priorities), and it stays marked "proposed, to confirm" until the user confirms it.

**Persistence.** The tree lives in `clarify-tree.md` in your scratchpad directory, not only in the conversation: a `/compact` prunes earlier turns, and a tree held only in memory loses its settled decisions. Write it with the Write or Edit tool when it is first laid out, rewrite it after every change of a decision's status, and at the end. Before resuming (new turn, interruption), reread it first rather than trusting what remains of the conversation.

## Step 3 — Rounds

The **frontier** is every open decision whose prerequisites are settled — askable now without guessing an unheard answer; a question depending on another open one waits for a later round.

**Fact-finding is never the user's job.** Anything answerable by looking (codebase, backlog, `.vibe/`, configs, manifests) is found instead, always by a dispatched sub-agent (Agent tool, `general-purpose`), never by reading or searching yourself, even for a single file. Don't block the round on it; only the questions that depend on that fact wait.

A constraint the user states ("the snapshots must not change", "it must stay compatible") is not a fact about the code: it says what must stay true, not what the solution must do about it. Before asking a risk question, or recording a deviation that constraint would force, have the sub-agent test the hypothesis when it is cheap (read the data, run the tests, try the simplest variant): if the constraint forces nothing, there is no question and no deviation. Ask the user only what the code cannot say.

Ask the whole remaining frontier in one round, numbered, each with your recommended answer:

```
❓ **Q1** - **<question title>**: <question body, possibly with choices>

➡️ <your recommended answer>

---

❓ **Q2** - ...
```

Then stop and wait for the user's answers before asking the next round or acting on anything. Each answer settles a decision, with its priority, and may unblock others; a sub-agent's finding is folded in the same way. The tree is not only additive: a free answer that contradicts a decision already settled reopens that decision and its sub-branches before the round continues. Recompute the frontier, rewrite the tree file, and repeat.

## Modes `need` and `implementation`

The build workflow (`vibe:feature`, `vibe:fix`) calls this skill twice, with the mode on the first line of `$ARGUMENTS`: `mode: need`, then `mode: implementation`. Without that line, the protocol above applies as is, to both spaces at once (the standalone use of `backlog`, `init` and `workspace-init`).

| Mode | Space | Question | Where to look first |
|---|---|---|---|
| `need` | problem space | What must be solved, for whom, under which business constraints? | The brief, the backlog item and its acceptance criteria, `.vibe/` (`index.md`, `glossary.md`, `decisions/`), the project memory directory the session indicates |
| `implementation` | solution space | Which approach, under which technical constraints? | The code, its tests, its configuration, `CLAUDE.md`, `.vibe/modules/`; then the expert consultation the caller passes (its `REQUIREMENTS` and `RISKS` are sources, not questions) |

In both modes, four rules are added:
1. **Look before asking.** The user is a Product Owner: a question reaches them only when its answer is in none of the mode's sources. Read them (through the dispatched sub-agent, as in Step 3) before the first round. A round with no question left is normal: the mode then ends at once.
2. **Source every answer you give yourself.** A decision settled without a question cites its source in the report — `(source: path:line)`, the sentence of the brief, the memory entry. The caller has these claims checked; a decision with no source is a guess.
3. **Say when it takes a spike.** When several decisions of the same round depend on one another and no source settles them, and the answer has to be **searched or tried** (compare libraries, check what an external system accepts, measure) rather than preferred by the user, do not ask the user to pick: end with `CLARIFY-RESULT: partial — spike: <the question to settle first>` and let the caller decide. Do not recommend a library or a format yourself in that case.
4. **Stay in your space.** In `need`, no decision about code, files or approach; in `implementation`, no decision about what the product does. A question that belongs to the other space is noted in the report as `(other space)` and left to that mode.

The `need` mode ends when its decisions are settled, without acting on them: the `implementation` mode, then the caller, execute.

## Step 4 — End

When the frontier is empty, summarize the shared understanding and ask the user to confirm it before treating it as final or handing it to a caller. If the user stops early (declines to continue, says the rest does not matter), respect that and report what was settled, flagging the rest as open.

## Step 5 — Report

One report for both audiences — the human, and a caller skill that parses the literal headings:

```
CLARIFY-RESULT: settled
### Synthesis
[2–5 plain sentences, in the conversation's language, folding every settled decision into one description of the subject — written to directly replace the caller's original input]

### Decisions made
- **[question title]** (🔒 MUST): [answer reached]
- **[question title]** (⚖️ SHOULD): [answer found without asking] (source: path:line)
```

In a mode, the first line is `CLARIFY-RESULT: settled — mode: need` (or `implementation`). Ended early → `CLARIFY-RESULT: partial — [what is still open]` with the content actually reached. Nothing settled at all → `CLARIFY-RESULT: abandoned`, no sections; the caller falls back to its original input.
