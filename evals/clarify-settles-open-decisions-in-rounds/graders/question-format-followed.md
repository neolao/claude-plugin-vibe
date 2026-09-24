---
type: regex
target: trace
pattern: "❓\\s*\\*\\*Q1\\*\\*\\s*-\\s*\\*\\*[^<*][^*]*\\*\\*:[\\s\\S]*?➡️\\s*[^<\\s]"
weight: 1
---

Round 1 must follow the skill's exact numbered-question contract: a
`❓ **Q1** - **<title>**:` heading with a `➡️` recommended answer underneath
it, not free-form prose questions.

It reads the whole trace, not the last message: once the fact-finding
sub-agent runs, Round 1 is printed before it returns, and the final message
may only carry the later rounds. The `[^<…]` guards skip the skill's own
template (`**<question title>**`, `➡️ <your recommended answer>`), which the
trace also contains.
