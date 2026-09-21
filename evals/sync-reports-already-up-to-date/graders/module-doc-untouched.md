---
type: llm
focus: { source: file, path: ".vibe/modules/auth.md" }
criteria: |
  The file's content must be EXACTLY identical, character for character
  (including line breaks and spacing), to this reference text:

  # Module: auth
  **Role:** Authenticates a user and issues a session.
  **Files:** `src/auth/index.js`
  **Exports:** `signIn(email, password): { email, session }`
  **Depends on:** (none)

  PASS only if the file matches this reference exactly, with no added,
  removed, reordered, or reworded lines.
  FAIL on any deviation, however small — including a merely equivalent
  rewording.
weight: 2
---

Nothing changed under `src/`, so the module doc must stay byte-for-byte as it
was.
