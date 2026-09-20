# Eval history

Tracks `claude plugin eval` scores over time — one row per meaningful run, so a
model or agent-definition change can be compared against what came before.
Full reports (`report.html`, `aggregate-result.json`) are regenerated on every
run and gitignored; this file is the only thing kept.

Cost and tokens matter alongside the score: two runs with the same score are
not equal if one gets there for fewer tokens/$. Cost comes straight from the
CLI's own totals (agent + judge, summed over the case's runs). Tokens require
extra work the CLI doesn't do on its own — see below — so older rows logged
before this practice started show `n/a`.

**How to get the token figures:** re-run the case with `--keep-temp` (no
extra API cost — it only skips deleting the sandbox). For each kept dir,
`chmod 700 <dir> <dir>/sealed`, then read the last `type: result` line of
`<dir>/out/trace.jsonl` — its `modelUsage` object breaks tokens down per
model (in = `inputTokens + cacheReadInputTokens + cacheCreationInputTokens`,
out = `outputTokens`). Sum across models, then across the case's runs, and
`rm -rf` the kept dirs once done — they are not meant to be preserved.

| Date | Agent | Agent version | Case | Model | Score | Pass rate | Cost (N runs) | Tokens in/out (N runs) | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-20 | review-security | 1.0.0 | review-security-finds-vulnerabilities | haiku | 1.00 | 3/3 | $0.29 | n/a (pre-tracking) | Finds the hardcoded secret, both injections, and the weak hash; follows the FILE/CATEGORY/SEVERITY contract |
| 2026-09-20 | review-security | 1.0.0 | review-security-no-false-positives | haiku | 1.00 | 3/3 | $0.29 | n/a (pre-tracking) | No false positive on env-sourced key, parameterized query, list-form subprocess, bcrypt, or `.env.example` |
| 2026-09-20 | review-solid | 1.0.0 | review-solid-finds-violations | haiku | 0.95 | 2/3 | $0.33 | 163,573 / 10,765 | Reliably finds S, O, L, D; misses the ISP finding (8-field `User`, 2 fields read) on 1 of 3 runs |
| 2026-09-20 | review-solid | 1.0.0 | review-solid-no-false-positives | haiku | 0.78 | 2/3 | $0.27 | 179,351 / 8,202 | On 1 of 3 runs, invents an `I`/ISP finding on `UserContact.format_greeting`, claiming it uses only 2 of the dataclass's fields when those are its only 2 fields |
