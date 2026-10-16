---
name: learn
description: Turns a correction, refusal, or constraint about how Claude works — stated in general terms ("always", "never", "every time", "from now on", "stop doing", "in every project") or repeated in the session ("again", "I already told you") — into a one-line global rule in ~/.claude/rules/, after the user confirms; load it on reading such a message, before answering and before any project memory, even when the instruction rides along another request, and again when the protocol is already in progress (rule confirmed or declined). Not for an isolated local correction ("here, rename X") nor for a fact that only holds in one project.
argument-hint: "[optional: the rule to save; empty infers it from the correction just given]"
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:learn — Global Rules From Corrections

Capture a cross-project working preference as a global rule in `~/.claude/rules/`, Claude Code's cross-project rules folder: every `.md` file there is loaded in every session of every repository. Everything said to the user is written in the language the conversation is being conducted in — never a fixed one.

## Step 1 — Trigger and threshold

Activate as soon as the user:
- corrects a bias, a response habit, or a turn of phrase;
- states a recurring constraint on method, format, or tooling;
- refuses a deliverable or asks for an adjustment to the way of working.

**Threshold:** only when the correction is stated in general terms ("always", "never", "every time") or repeats within the session. An isolated local correction ("here, do X instead") triggers nothing — otherwise a review with five local fixes costs five interruptions.

**In addition to the answer, never instead of it.** Apply the instruction from the first word of the current answer (an instruction about how to open or format an answer already applies to this one), handle the request it came with, and redo the deliverable the correction targets in this same answer under the new instruction — if it is no longer visible in context, rebuild it from what the user says about it rather than asking them to share it again. The procedure below is added to that answer.

**Priority over auto-memory.** A cross-project preference goes to `~/.claude/rules/`, never to the project's memory folder — do not read or write auto-memory for this kind of instruction. A fact that only holds in one project belongs to that project's memory — `/vibe:debrief`'s territory, not this skill's.

## Step 2 — Target file

Rules are split by nature across three files in `~/.claude/rules/`:
- `vibe-preferences.md` — communication habits, tone, concision, biases to avoid.
- `vibe-workflow.md` — validation process, memory handling, planning and sub-agents.
- `vibe-technical.md` — output conventions, formats, syntax, typography.

Several instructions in one message → one rule each, each in its own file.

## Step 3 — Isolate, categorise, deduplicate

1. **Isolate** — phrase the rule as one concise, universal, imperative line.
2. **Categorise** — pick the target `vibe-*.md` file (create the folder and the file if absent, at Step 5).
3. **Deduplicate** — reread the target file if it exists. A rule already covering the same dimension (two answer-length limits, even in different units) is replaced by the updated version, keeping whatever else it said, instead of adding a redundant bullet: never leave two contradictory or stale rules side by side. An unreadable file (absent, access denied) blocks nothing: move on.

## Step 4 — Confirm, then stop

Submit the one-line rule through `AskUserQuestion` — "Save as a global rule, valid in every repository?" — quoting the rule and its target file, before any write. Without `AskUserQuestion`, ask the same question in text at the end of the answer. Then **stop**: no write in this turn, and no prior check of the write tools — the question does not depend on them. A one-off correction is not necessarily a universal preference; this file is loaded in every session, everywhere, and a badly generalised rule is costly.

The user declines → write nothing. The user already confirmed (in the message itself, or earlier) → do not ask again, but still run Step 3's deduplication before Step 5.

## Step 5 — Persist

Add (or replace) the rule as a bullet, without touching the other rules. Before writing, reread the final content: no two bullets may cover the same dimension.

## Step 6 — Notify

Only in an answer that follows the user's reply to Step 4's question (or a confirmation/refusal already given) — the answer that **asks** the question carries no `🗒` line. End that answer with exactly one of these lines, copied word for word, as the very last line — nothing after it, nothing added between the brackets:
- `🗒 [Global rule saved to ~/.claude/rules/vibe-<category>.md]` — the rule was written;
- `🗒 [Global rule not saved — declined by the user]` — the user said no at Step 4, never for any other reason;
- `🗒 [Global rule not saved — write failed]` — the user confirmed but the write failed: only after a `Write`/`Edit` actually attempted and refused, or when no write tool exists — a failed read is not enough.

Any other remark (a suggestion for project memory, etc.) goes **before** that line.

## Guardrails

- **Scope:** writes only in `~/.claude/rules/`.
- **Universal only:** never store an instruction tied to a project's business context or specifics — a rule must stay true whatever repository is open.
- **Nothing else in that folder:** never put any other `.md` in `~/.claude/rules/` — Claude Code loads every `.md` there as a global rule.
