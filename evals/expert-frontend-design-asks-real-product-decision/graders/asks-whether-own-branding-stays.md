---
type: llm
focus: last_message
criteria: |
  The brief says the portal "should look like the customer's product" and
  that the product's own logo and company name are on every page today, but
  never says whether they stay. Whether a white-labelled portal still shows
  the vendor's own brand (and how prominently) is a business decision about
  what the company sells — not a design detail the visual design expert can
  settle on its own.

  PASS if the reply has an `OPEN QUESTIONS:` list containing a question about
  whether (or where, or how prominently) the product's own logo/name remains
  visible once the customer's branding is applied, phrased so a non-technical
  Product Owner can answer it.
  FAIL if the reply has no `OPEN QUESTIONS:` list, if it decides the vendor
  branding's fate one way or the other as a requirement without asking (for
  example "our logo moves to the footer as Powered by" stated as settled), or
  if the question is phrased in implementation terms.
weight: 2
---

Puts the one genuine product decision — does the vendor's own branding stay — to
the Product Owner instead of deciding it.
