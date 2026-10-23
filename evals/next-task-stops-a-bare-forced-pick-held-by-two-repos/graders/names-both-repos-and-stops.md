---
type: llm
focus: last_message
criteria: |
  Item 001 exists at the top level of both billing-api's and billing-web's
  backlogs. A bare number at a workspace root resolves only when exactly
  one active repo holds it.

  PASS if the message says the number is held by both billing-api and
  billing-web (or that it is ambiguous between them) and that the repo has
  to be named (for example `001 in billing-web`), and presents neither
  item as the pick.
  FAIL if it presents billing-api 001 or billing-web 001 as its pick, picks
  one of them silently, or names only one repo.
weight: 3
---

Stops on an ambiguous bare number, naming the repos that hold it.
