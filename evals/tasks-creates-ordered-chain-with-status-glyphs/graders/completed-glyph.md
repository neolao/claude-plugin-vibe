---
type: regex
target: last_message
pattern: "✓\\s*Write tests"
weight: 1
---

The `completed` transition used the exact `✓ <subject>` glyph line the
skill specifies, not paraphrased prose like "Finished Write tests".
