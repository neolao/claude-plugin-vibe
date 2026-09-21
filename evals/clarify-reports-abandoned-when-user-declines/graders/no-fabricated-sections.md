---
type: regex
target: last_message
pattern: "### Synthesis|### Decisions made"
match: not_contains
flags: i
weight: 2
---

Step 5 is explicit: an abandoned run gets no sections at all. Neither a
`### Synthesis` nor a `### Decisions made` heading may appear — there is
nothing settled to summarize, and inventing one would hide that from the
caller/user.
