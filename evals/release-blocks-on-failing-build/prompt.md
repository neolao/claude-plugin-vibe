---
name: release-blocks-on-failing-build
description: >-
  vibe:release must run the pre-release build command and stop, without
  cutting a version, when it fails. Requires --allow-tools Bash,Write,Edit
  to run (Bash/Write/Edit are gated tools).
tags: [release, build-gate]
runs: 3
max_turns: 25
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:release` skill (Skill tool, `skill: "vibe:release"`) with no
arguments, so it reads `CHANGELOG.md` itself and suggests the version bump.

This is a non-interactive eval: if the skill asks you to confirm the
suggested bump before running its pre-release checks, confirm it. Its
pre-release checks include a build command that fails deterministically in
this fixture — do not work around it, do not edit `package.json`'s `build`
script to make it pass, and do not fix the (fictitious) underlying build
error yourself. Follow the skill's own instructions for a failing
pre-release check exactly as written.

Once the skill has stopped (or otherwise concluded), run `git tag` and
`git log --oneline -5` with the Bash tool and include their raw output in
your final message. Then report, in short plain sentences, what the skill
found and did.
