---
type: llm
focus: { source: file, path: docs/architecture.md }
criteria: |
  PASS only if docs/architecture.md is a substantial, developer-facing
  description of the real module layout of this project: it names the
  `commands` and `storage` modules (or the actual file paths
  src/commands/ and src/storage/), states each module's responsibility, and
  describes how they interact (commands read/write widgets through the
  storage module).

  FAIL if the file is empty, near-empty, generic boilerplate that could apply
  to any project, or a paraphrase of a project index / README rather than a
  genuine description of this project's own code structure.
weight: 2
---

The generated architecture doc gives a real reading of the code, not a
placeholder or a reworded copy of another source.
