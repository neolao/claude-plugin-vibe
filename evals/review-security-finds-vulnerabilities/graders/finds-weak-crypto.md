---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Crypto` finding on `hash_password` using
  `hashlib.md5` to hash a password, recommending bcrypt/scrypt/argon2 instead.
  FAIL if the MD5 password hashing is not flagged.
weight: 1
---

Reports the MD5 password hashing as a Crypto finding.
