---
name: debrief
description: End-of-task retrospective turned into durable memory — asks the user 1–3 short questions about the task just finished, then records each preference, correction or project fact in the project's memory directory. Trigger on "debrief", "retro", "what should I remember from this", or at the end of a substantial task (the build workflow invokes it after its report). Not for a one-off question, a read-only exchange, a one-line fix, or a cross-project rule (that is /vibe:learn).
argument-hint: "[no argument — runs on the task just finished in this conversation]"
version: 1.0.0
model: claude-sonnet-5-5
---

# /vibe:debrief — Closing Retrospective

A lesson learned during a task must not stay in the conversation: it has to outlive the terminal. This skill asks the user a few targeted questions about the task just finished and turns the answers into memories the next session will read.

Run it only after a substantial task — the build workflow invokes it after its report, outside `--auto`. Never for a trivial exchange (a one-off question, a read-only task, a one-line correction): a debrief costs the user attention and is worth it only when something deserves to be kept.

Boundary with `/vibe:learn`: a cross-project preference ("always…", "never…") is a global rule and belongs to `/vibe:learn`; a fact or preference tied to this project is this skill's.

Everything said to the user is written in the language the conversation is being conducted in.

## Step 1 — Ask

Ask 1 to 3 short retrospective questions with `AskUserQuestion`, fitted to what actually happened — `${CLAUDE_PLUGIN_ROOT}/skills/debrief/references/questions.md` gives example wordings per family. Ask only what is relevant: no question about hesitations when there were none. Each question offers 2–3 concrete moments or choices of the task as options, plus "Nothing to report"; the free-text field covers the rest — the tool accepts no question without options.

If `AskUserQuestion` is not available, ask the same questions in text (numbered, same concrete options) and **stop**: without an answer, search no memory, write nothing, and show no closing block. Never invent an answer on the user's behalf. Steps 2 and 3 resume once the user has answered.

## Step 2 — Capture

For each answer that reveals a preference, a correction or a project fact not derivable from the code, in this order:

1. Look for an existing memory that already covers the subject, in the project memory directory the session indicates (list `MEMORY.md` and its neighbours); update it rather than create a duplicate.
2. Otherwise write a new memory in the harness's standard format: frontmatter `name` / `description` / `metadata.type`, body with **Why:** and **How to apply:** — the labels the harness uses for the memories it writes itself in the same directory.
3. Add a line to `MEMORY.md` pointing to that file. This step is mandatory and distinct from (2): attempt it even if (2) failed (for instance a permission error on the individual file) — the index is never silently skipped because the previous write failed. If (2) or (3) fails, say so explicitly in the final reply rather than abandon the debrief without explanation.

If the session indicates no memory directory, say so and write nothing.

If no answer justifies a write (nothing new, nothing surprising), write nothing — the debrief can close with no memory created.

## Step 3 — Closing block

End with one block:

```
📝 Debrief — [N memory(ies) captured in <path> | nothing to capture]
```
