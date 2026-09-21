---
name: clarify-settles-open-decisions-in-rounds
description: >
  clarify must map "let users export their data" as a design tree, dispatch
  a sub-agent to find the one fact answerable by reading .vibe/glossary.md
  (that a user's data is scoped to exactly one Workspace) instead of asking
  the user, ask the genuinely open product decisions (export format, scope
  of "their data" vs. shared content, sync vs. async) in the skill's
  `❓ **Q1**` / `➡️` numbered format, and — once given clear answers — reach
  `CLARIFY-RESULT: settled` with a `### Synthesis` that actually folds those
  answers in rather than restating the original vague request. Needs
  --allow-tools AskUserQuestion to run.
tags: [clarify, settles, fact-finding]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Agent, AskUserQuestion]
---

Invoke the `vibe:clarify` skill (Skill tool, `skill: "vibe:clarify"`) with this subject: "let users export their data".

This is a real, deliberately underspecified feature idea. It has several genuinely open product decisions nobody has made yet — at least: what format the export uses, whether "their data" means only content a user personally owns or also content shared with them inside a Workspace, and whether the export is delivered synchronously (immediate download) or generated asynchronously (a job the user is notified about later). It also has one fact buried in this repo that is not a product decision at all and should be found by reading, not asked to you: `.vibe/glossary.md` already documents how a user's data is scoped (see its "Workspace" entry).

When `vibe:clarify` presents its Round 1 questions in its own `❓ **Q1**` / `➡️` numbered format, do not wait for a separate message — answer every question yourself, right away, with clear and decisive choices (for example: pick one concrete export format, state plainly whether shared Workspace content is in or out of scope, and pick sync or async — you do not have to follow its recommended answer, but do not equivocate or say "I don't know"). If a later round asks anything further, answer it the same way, decisively, until `vibe:clarify` reaches its end state.

In your final message, reproduce `vibe:clarify`'s entire run verbatim: every round of questions it asked, the answers you gave, and its closing report (the `CLARIFY-RESULT:` line and everything under it).
