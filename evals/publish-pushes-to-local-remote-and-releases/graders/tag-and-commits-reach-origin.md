---
type: regex
target: last_message
pattern: "v1\\.0\\.1"
weight: 2
---

The prompt instructs Claude to run `git ls-remote --tags origin` after
`vibe:publish` finishes and report the output. The local bare "origin"
repo must have actually received the new `v1.0.1` tag (bumped from the
existing `v1.0.0`) — not just a local commit and tag that stayed unpushed.
