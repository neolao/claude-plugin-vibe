---
type: regex
target: trace
pattern: "refused: \\S+ has no \\.vibe/ directory"
weight: 1
---

The usage report was written at the end through the `vibe:usage-report`
script. The fixture has no `.vibe/`, so the script's `write` refuses with
this line: it appears only if the write was attempted. A regex on the
script's output, not on the command, because the command is often built
from shell variables.
