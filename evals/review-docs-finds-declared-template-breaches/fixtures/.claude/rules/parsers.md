---
paths:
  - "src/parser/**"
---

A reader yields `Transaction` records and never touches the database; a bank-specific quirk is handled in the reader and nowhere else.
