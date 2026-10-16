---
name: changelog-reads-a-merge-of-throwaway-commits
description: "/vibe:changelog must announce the PDF export under Added when the only description of the work is the merge message of a pull request whose commits are wip, fixup and typo — without copying those words or the merge boilerplate — and still record the fix made on main under Fixed. Requires --allow-tools Bash,Write,Edit to run."
tags: [changelog, merge]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:changelog` skill (Skill tool, `skill: "vibe:changelog"`) with no arguments, on the git repository in this workspace.

Once it finishes, report exactly what it changed.
