---
name: verify
description: Definition-of-Done check of a deliverable (code, document, plan, analysis, recommendation) against the user's original request — three parallel read-only control grids (scope, rigor, finish), fixes, then a mandatory closing block. Trigger on "is it complete", "is it ready", "ready to merge / to ship / to send", "check this", or whenever a deliverable is produced outside /vibe:feature and /vibe:fix. Not for a one-off question, an explanation, a read-only task, or a one-line correction.
argument-hint: "[optional: what to check — a file, a diff, a document, or the deliverable under discussion; empty infers it from the conversation]"
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:verify — Definition of Done

Check a deliverable against the request that produced it, through three control grids run in parallel by read-only sub-agents, and prove the check ran with a closing block. `/vibe:feature` and `/vibe:fix` already carry TDD, runtime verification and review: `/vibe:verify` is for everything produced outside them — a document, a plan, an analysis, a recommendation, ad-hoc code — or for when the user asks whether something is complete or ready.

**Golden rule:** never end the turn without having run the three grids. A reply that contains the deliverable but not the closing block breaks this rule.

Everything said to the user is written in the language the conversation is being conducted in; the closing block is the one fixed text.

## Step 1 — Deliverable

`$ARGUMENTS` if non-empty (a file, a diff, a document, a description of what to check); otherwise the deliverable produced or discussed right before this skill was invoked.

If the deliverable does not exist yet (the user asked for something and nothing has been written), produce it entirely yourself, with your own tools: launch no sub-agent to write, run or test it — a sub-agent has no more tools than you, and its replies are not grid verdicts. The only sub-agents of this skill are the three grids of each pass. Do not add clarification questions the request does not call for.

If file-writing tools are unavailable, the deliverable is the text of your reply: the grids audit that text, and you deliver it in the same message as the closing block.

## Step 2 — Task list

Before producing anything, invoke the `vibe:tasks` skill with three chained tasks:

```
Produce the deliverable ← no dependency
Pass 1 — three grids ← blockedBy "Produce the deliverable"
Closing block ← blockedBy "Pass 1 — three grids"
```

The three grids of a pass are one task: they run in parallel, and nothing tracks them separately. If a task list already exists, append these tasks to it; if it already holds the tasks that produce the deliverable, those stand in for `Produce the deliverable` — create only the other two, with `Pass 1 — three grids` blocked by each production task still open. If the deliverable already exists when the skill starts, mark `Produce the deliverable` completed at once. Grids are read-only: only the main agent moves tasks.

## Step 3 — Run the three grids

As soon as the deliverable is written, your very next tool call is the Agent tool for the three grids. Never present the deliverable to the user, conclude, or yield between producing it and the closing block.

Launch three agents in one message (Agent tool, `subagent_type: "general-purpose"`, `model: "haiku"`, `run_in_background: false` — without it the verdicts do not reach your reply; never launch a placeholder agent to wait for them). These grids exist only for this skill and are never invoked elsewhere:

- Scope grid — `${CLAUDE_PLUGIN_ROOT}/skills/verify/references/grids/scope.md`
- Rigor grid — `${CLAUDE_PLUGIN_ROOT}/skills/verify/references/grids/rigor.md`
- Finish grid — `${CLAUDE_PLUGIN_ROOT}/skills/verify/references/grids/finish.md`

Each prompt opens with the read-only sentence — "You are a read-only control grid: modify no file, run nothing that changes state, only report. Do it yourself: invoke no skill and launch no agent." — then contains:

- the full content of the grid file;
- the user's **original request**, quoted **verbatim** — never paraphrased: a paraphrase would carry the same misreading as the deliverable — plus the explicit constraints the user set; the sub-agent does not see the conversation and cannot judge conformity without this;
- the deliverable to audit: the text itself for a reply or a document; for code, the paths of the changed files or the `git diff` — the sub-agent reads them, do not paste the content inline;
- the format instruction, word for word: "Your reply starts with `[PASS]` or `[FAIL]` — that bracketed word is the very first thing, before any title or sentence. For `[PASS]`, then cite one piece of evidence per checklist item; for `[FAIL]`, list the required corrections."

## Step 4 — Handle the verdicts

**Any `[FAIL]`** on one or more grids: apply the corrections, then rerun **all three grids** on the corrected deliverable — a `[PASS]` obtained on an earlier version is void. **Three complete passes maximum** (a pass = the three grids on the same version of the deliverable). If a grid still fails on the third pass, stop rerunning and close with the failure block below. Task bookkeeping: mark the failed pass completed (it did run), create `Fixes pass N` and `Pass N+1 — three grids`, chained, and re-block `Closing block` on the new pass.

**Exception:** a correction that contradicts a decision the user took explicitly **after** the original request (the grid only sees that request and cannot know it) is not applied — pass that decision to the grid on rerun, and record the deviation in the closing block.

**Non-binary verdict:** a reply that starts with neither `[PASS]` nor `[FAIL]`, or contains both — "PASS with reservations", a free audit with ✓ marks, no tag at all — counts as `[FAIL]`, however favorable it looks. A tool error reruns that one grid without consuming a pass.

## Step 5 — Closing block

Mark `Closing block` completed, then end your last message with one of these two exact blocks and write nothing after it (no status line, no remark, no file list).

All three grids `[PASS]`:

```
---
🛡️ DoD — Scope ✅ · Rigor ✅ · Finish ✅
✅ [DoD passed]
---
```

A grid still `[FAIL]` after three passes (❌ on each failing grid):

```
---
🛡️ DoD — Scope ✅ · Rigor ❌ · Finish ✅
⚠️ [DoD not passed] — Rigor: <summary of the last [FAIL]>
---
```

In both forms, each correction set aside under the exception above adds one line before the final `---`: `↪ Intended deviation — <grid>: <user decision>`.

The block appears only when this skill actually ran: its absence means no check took place. `/vibe:debrief` may add its own block after this one.
