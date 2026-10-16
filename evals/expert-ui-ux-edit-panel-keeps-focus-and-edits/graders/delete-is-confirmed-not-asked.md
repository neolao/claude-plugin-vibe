---
type: llm
focus: last_message
criteria: |
  The brief says a deleted product is gone for good and that adding a trash
  or archive is not part of this change. The expert's own checklist settles
  the rest: a destructive action is confirmed or undoable, and undo is ruled
  out here. So the confirmation is a requirement, and whether to confirm, or
  whether to add a trash, is not a question for the Product Owner.

  PASS if REQUIREMENTS or TEST SCENARIOS requires a confirmation step (or an
  equivalent safeguard, such as typing the product name, or a Delete button
  that cannot be reached by the same keystroke sequence as Save) before the
  permanent deletion, tied to this panel's Delete button, and no
  `OPEN QUESTIONS:` entry asks whether deletion should be confirmed,
  reversible, or go to a trash or archive.
  FAIL if the permanent deletion gets no safeguard, or if the confirmation,
  an undo, or a trash or archive appears as an `OPEN QUESTIONS:` entry.
weight: 2
---

Requires a confirmation before the permanent delete, as a requirement and
not as a question the brief and the checklist already settle.
