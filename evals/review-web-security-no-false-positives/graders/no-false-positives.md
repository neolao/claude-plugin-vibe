---
type: llm
focus: last_message
criteria: |
  The fixture uses only safe patterns that superficially resemble each
  checklist category's vulnerable shape without being exploitable:
  - `download_file` sanitizes the name with `secure_filename` and then
    re-checks the resolved real path still starts inside `UPLOAD_DIR`
    before serving it (not Path traversal).
  - `search` escapes the `q` parameter with `markupsafe.escape` before
    embedding it in HTML (not XSS).
  - `set_nickname` strips everything outside a safe character set before
    writing into the `X-Nickname` header (not Header injection).
  - `delete_user` is wrapped in a `require_admin` decorator that checks an
    admin token before running (not Access control).
  - `fetch_avatar` checks the target hostname against an explicit
    `ALLOWED_AVATAR_HOSTS` allowlist before fetching (not SSRF).
  - `report` clamps `rows` to a fixed maximum regardless of client input
    (not DoS).
  - `login`'s `session_id` cookie is set with `httponly=True, secure=True,
    samesite="Strict"` (not Cookies).
  - `whoami` returns a generic error message and only logs the real
    exception server-side (not Info disclosure).
  - `add_security_headers` actually sets CSP, X-Content-Type-Options,
    X-Frame-Options, and Strict-Transport-Security on every response (not
    Security headers).

  PASS if the response reports no `high` or `medium` severity finding in any
  of the review-web-security checklist categories on this code — either no
  findings at all, or only `low` severity style notes unrelated to these
  already-safe patterns.
  FAIL if it flags any of the nine safe patterns above as vulnerable (e.g.
  calling the containment-checked file read a traversal, the escaped search
  output XSS, the allowlisted fetch SSRF, the hardened cookie unsafe, or the
  present security headers missing).
weight: 2
---

Does not invent web-security findings on code that already follows the
safe pattern for each category.
