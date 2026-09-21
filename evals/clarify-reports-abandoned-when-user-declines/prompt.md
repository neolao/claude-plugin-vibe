---
name: clarify-reports-abandoned-when-user-declines
description: >
  clarify must report CLARIFY-RESULT: abandoned, with no fabricated
  Synthesis or Decisions-made sections, when the user declines to answer
  its very first round of questions instead of pushing ahead and inventing
  a plan. Needs --allow-tools AskUserQuestion to run.
tags: [clarify, abandoned]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Agent, AskUserQuestion]
---

Invoke the `vibe:clarify` skill (Skill tool, `skill: "vibe:clarify"`) with this subject: "make the app faster".

This is a deliberately vague subject with no fixed scope — plenty of open decisions (which part of the app, what "faster" means, for which users) and nothing has been decided yet.

When `vibe:clarify` presents its Round 1 questions, do not answer them. Instead, decline to continue: say plainly, in your own words, that you don't want to answer these questions right now and would rather stop the interview here — the way a real user might cut it short. Do not answer any of the questions, even partially, and do not ask `vibe:clarify` to guess on your behalf.

In your final message, reproduce `vibe:clarify`'s entire run verbatim: the round of questions it asked, your decline, and its closing report.
