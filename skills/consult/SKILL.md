---
name: consult
description: Reasoned opinion from one of the plugin's experts on a precise point (architecture, UI/UX, API, data, ops…) outside a feature or fix — one read-only consultation, the user decides; not for reviewing a diff, attacking a settled decision, or a local detail with no structural stake
argument-hint: "[domain: architecture | ui-ux | frontend-design | api-rest | cli-dx | data | linux | ops | realtime-rendering] \"<precise question>\""
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:consult — Expert Opinion

Get a reasoned, outside opinion from one of the plugin's `vibe:expert-*` agents on **one** precise point: where to put a boundary, which pattern, which HTTP shape, which schema, how it should run in production. An opinion is worth its question and its context: without a precise point and real constraints it produces only generalities. Not for reviewing a diff (`/vibe:review`), attacking a decision already settled (`/vibe:challenge`), or a local detail with no structural stake — answer those directly.

Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — Pick the expert

If the first word of `$ARGUMENTS` names a domain (`architecture`, `ui-ux`, `frontend-design`, `api-rest`, `cli-dx`, `data`, `linux`, `ops`, `realtime-rendering`), that is the expert; the rest is the question. Otherwise match the question against the descriptions of the `vibe:expert-*` agents and pick the one whose domain clearly fits. If the question is vague ("what do you think of the architecture?"), ask for the precise point first — one question, not a `/vibe:clarify` tree — and wait.

## Step 2 — Build the dossier

As working notes:
- **The question**, in one sentence.
- **Context**: the system, its size, the stack.
- **Known constraints** (performance, deadline, compatibility, team).
- **Files or directories to read**, as absolute paths — located by you, never pasted as code: an opinion on existing code is grounded in that code.
- **What was already tried or rejected**, with the motive.

## Step 3 — Launch the expert

Launch **one** agent (Agent tool, `subagent_type: "vibe:expert-<name>"`, `run_in_background: false`, so the opinion comes back in this turn). Its prompt opens with this sentence verbatim: "Read-only: you modify no file and produce only an opinion. Do it yourself: invoke no skill and launch no agent." Then the dossier, then this request verbatim: "Reply in short sections: `Problem reading` (the question restated and the need behind it), `Options` (at least two, including the simplest; for each what it gains, what it costs, when it turns bad), `Recommendation` (one option, justified by the constraints), `Risks` (what breaks first, when, the cost of reversing), `To verify` (the facts that would change your recommendation). Cite `file:line` for anything about existing code. If there is not enough to decide, say so and list what is missing rather than invent a recommendation."

## Step 4 — Report

Report the opinion in full, without softening it: the recommendation and its reasons, the trade-offs, the risks, the alternatives with why they lost, what to verify before deciding. Then add your own view of what looks solid or debatable **in the real context** — the expert did not see this conversation. The user decides.

One pass, no loop: a sub-point worth digging into gets a new consultation.

End with:

```
---
🏛️ Expert <domain> — [Recommendation: <short summary> | No firm recommendation: <why>]
---
```
