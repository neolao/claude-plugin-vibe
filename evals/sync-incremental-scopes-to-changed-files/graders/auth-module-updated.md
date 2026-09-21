---
type: llm
focus: { source: file, path: ".vibe/modules/auth.md" }
criteria: |
  PASS if the module doc now documents a `signOut` export — for example
  listing `signOut(session)` or an equivalent signature under Exports, or
  otherwise clearly describing the new sign-out capability added to
  `src/auth/index.js`.
  FAIL if `signOut`, or an equivalent description of a sign-out export, is
  absent from the file.
weight: 2
---

`.vibe/modules/auth.md` must be refreshed to reflect the newly added
`signOut` export — the whole point of incremental mode is catching what
actually changed (recall).
