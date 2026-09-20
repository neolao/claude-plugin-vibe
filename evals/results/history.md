# Eval history

Tracks `claude plugin eval` scores over time — one row per meaningful run, so a
model or agent-definition change can be compared against what came before.
Full reports (`report.html`, `aggregate-result.json`) are regenerated on every
run and gitignored; this file is the only thing kept.

| Date | Case | Model | Score | Pass rate | Notes |
|---|---|---|---|---|---|
| 2026-09-20 | review-security-finds-vulnerabilities | haiku | 1.00 | 3/3 | Finds the hardcoded secret, both injections, and the weak hash; follows the FILE/CATEGORY/SEVERITY contract |
| 2026-09-20 | review-security-no-false-positives | haiku | 1.00 | 3/3 | No false positive on env-sourced key, parameterized query, list-form subprocess, bcrypt, or `.env.example` |
