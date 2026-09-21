---
name: publish-pushes-to-local-remote-and-releases
description: >
  vibe:publish pushes local commits to a local bare "origin" remote, decides
  the version bump from a Fixed-only CHANGELOG > Unreleased section, invokes
  vibe:release with an explicit "patch" argument (never blank), and the
  local remote ends up holding both the commits and the new tag. Never
  touches a real network host.
tags: [publish, e2e]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:publish` skill (Skill tool, `skill: "vibe:publish"`) with no
arguments.

Once it finishes, run `git ls-remote --tags origin` and report its exact
output in your final message, together with `vibe:publish`'s own report.
