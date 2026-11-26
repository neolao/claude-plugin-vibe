---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Entity` (or clearly equivalent
  category name) finding on `Member` in fixtures/studio/member.py for
  comparing members by value on all their attributes (the `@dataclass`
  default equality) although `Member` carries an identity, `member_id`.
  The finding may or may not spell out the consequence (a member whose email
  changed is no longer equal to the copy a session holds, so `enrol`'s
  duplicate check and `withdraw` miss it); either way it passes.
  FAIL if no finding flags `Member`'s equality, or if the only finding on
  `Member` is about something else (its `tier` string, a public field).
weight: 2
---

Reports the entity whose equality is by value on every attribute instead of
by its id.
