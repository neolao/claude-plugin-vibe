---
type: llm
focus: last_message
criteria: |
  The fixture uses only safe patterns: `API_KEY` read from `os.environ`, a parameterized
  SQL query (`?` placeholder), `subprocess.run` with a list of args and `shell=False`,
  `bcrypt` for password hashing, and a `.env.example` with placeholder values.

  PASS if the response reports no `high` or `medium` severity Secret, Injection, or
  Crypto finding on this code — either no findings at all, or only `low` severity
  style notes unrelated to these safe patterns.
  FAIL if it flags the env-sourced API key as a hardcoded secret, the parameterized
  query as SQL injection, the list-form subprocess call as shell injection, bcrypt as
  weak crypto, or the `.env.example` placeholders as committed secrets.
weight: 2
---

Does not invent security findings on code that already follows the safe pattern for
each category.
