---
type: llm
focus: last_message
criteria: |
  Since the tag: a feature commit that added a PDF export (and its own
  changelog entry), a fix, and a revert of the feature commit.
  PASS if the report says the PDF export and its revert cancelled each
  other out (or equivalent: dropped both, net effect none) and that the
  existing PDF entry was removed from [Unreleased].
  FAIL if the report claims a PDF export was added, claims a removal was
  recorded, or does not account for the revert at all.
weight: 1
---

The caller learns that an entry was taken out and why, instead of
discovering a silently shorter `[Unreleased]`.
