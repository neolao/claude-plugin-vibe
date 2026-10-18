---
name: rewrite
description: Rework an existing text for clarity by named rules — Williams, Clark & Haviland's given-new contract, Gibson's dependency locality, ISO 24495-1, Ousterhout for code comments — defect-by-defect rewrite, meaning-preservation check by a sub-agent, writes only after validation; the output is always in the source text's language. Triggers on "rephrase", "make this clearer", "this is unreadable", "too heavy", "improve the writing", "proofread this document", "simplify this paragraph". Not for writing new text, translating, spelling-only fixes, or reviewing code (the build workflow's internal review does that).
argument-hint: "[mode: direct] [sentence, paragraph, file path or folder — empty uses the text under discussion]"
version: 1.1.0
model: claude-sonnet-5-5
---

# /vibe:rewrite — Rework for Clarity

## Golden rule
A shorter sentence is not a clearer sentence. Flesch, Gunning Fog and SMOG score only the length of sentences and words — optimizing for them rewards a choppy text that forces the reader to rebuild the links that were just cut. This protocol works on what explains the cost of reading, never on what can be counted.

## When to run
On a text **that already exists** and that the user wants reworked. Not on a text to be produced: there, nothing can be diagnosed, and these principles belong to revision, not drafting — Williams is explicit, thinking about them while drafting prevents finishing.

Do not trigger for a translation, a spelling or grammar fix alone, or a code review (the code itself is never touched here — see the matching invariant; code review belongs to the build workflow's internal review).

## Scope & language
The target is one of five kinds, and the kind changes the protocol:

| Target | Diagnosis | Control sub-agent | Writing |
|---|---|---|---|
| A single sentence given inline | `sentence.md` | no — the user sees everything at a glance | none |
| A paragraph given inline | `sentence.md` | **yes** — re-merging sentences is exactly where a link gets invented | none |
| A document | `sentence.md` + `document.md` | yes | after validation |
| A source file | `sentence.md` + `code-comments.md` | yes | after validation |
| A corpus (> 3 files) | inventory first (step 2) | one per retained file | after validation |

**Direct mode.** A first line `mode: direct` in `$ARGUMENTS`, before the text, means the caller is a vibe workflow handing over text it has just produced (a report, a plan for the user) and wants it back clearer, without a dialogue. The protocol is the same up to the check (steps 1 and 3 to 5, no corpus inventory, the reader framed from what the caller says without a question); steps 6 and 7 change: no before/after table, no question, no file written. Return the rewritten text itself, then the questions to the author as a list the caller may surface, then the closing block in its `direct` form. Two check passes maximum, as always; a passage still contested stays in its original wording and is named in the block. Inline text only: a file path in direct mode is refused with one line.

**The output is always in the language of the source.** An English text stays English, a French text stays French, a Japanese text stays Japanese. Translating is not clarifying. Only the instructions of this skill are in English; the diagnosis, the before/after table and the questions to the author are written in the language the conversation is conducted in, and the proposed text itself in the language of the source.

## Behaviour

1. **Frame the reader.** Identify the target reader and their goal (ISO 5.1.2 / 5.1.3) — "clear" means nothing without a reader: the same paragraph is limpid for a developer on the team and opaque for a customer. If the context does not allow it to be inferred, ask **a single** question via `AskUserQuestion`; this is not `vibe:clarify`, there is no tree to build here.

2. **On a corpus (> 3 files), inventory before rewriting.** Render a table "file → number of defects per family", then ask via `AskUserQuestion` which files to rework — a rewrite proposal over fifty documents is unreadable, and the user usually has only a few files in mind.

3. **Diagnose before rewriting.** Read the target, list the **located** defects, each labelled with the rule that explains it (`W2`, `GN1`, `G3`, `ISO 5.2.2`, `OUST-2`) — a global rewrite "by feel" can be neither checked, nor discussed, nor refused point by point.

   The diagnosis is a list, **one entry per defect**: the passage quoted between quotation marks, the rule identifier taken from a grid, what the defect costs the target reader. A sentence carrying two defects has two entries; an overall observation ("the whole text is nominal: W2") does not replace the entries, it can only introduce them. For the survey, ask two questions of every sentence of the original: **who acts**, and **what is the action**. An actor named anywhere other than as subject (in an agent complement, "by the security team", or in a noun or verb complement, "with the referent", "to the requester") or named nowhere is a `W1` entry, even if the rewrite keeps the construction; an action carried by a noun is a `W2` entry.
   - [references/sentence.md](references/sentence.md) — **always**. Sentence and paragraph level: Williams, given-new contract, dependency locality theory.
   - [references/document.md](references/document.md) — as soon as the target is a whole document or a corpus. Document level: ISO 24495-1.
   - [references/code-comments.md](references/code-comments.md) — **only** if the target is a source file.

   Each grid carries its own counter-rules section. Read them with the rules, not after: that is what prevents over-correction.

   Also record, one by one, the **missing links**: a subject arriving without an antecedent, a fact juxtaposed with no stated relation to the previous one, a noun or a verb without the complement the target reader needs ("a cache" of what, "measured" what, "the load" of what). Go through every sentence of the original for these links, one at a time, before rewriting anything. Each one will be either restored with the words of the original, or carried as a question to the author at step 6 — never neither.

4. **Rewrite defect by defect**, under the invariants below, following the order of application given at the end of `sentence.md` when several rules contradict one another on the same passage. Re-merging sentences is not condensing them: no load-bearing word removed, no shorter construction substituted for the original — no pronoun or auxiliary dropped, no relative clause reduced to a participle ("A cache exists. It is invalidated on deployment." becomes neither "has a cache invalidated on deployment" nor "A cache exists, invalidated on deployment").

5. **Have it checked.** Launch an agent via the Agent tool with `subagent_type: "general-purpose"`, `model: "sonnet"` and `run_in_background: false` — this is judgement on meaning preservation, not checklist ticking, and its verdict must come back within this same turn. The `prompt` opens with "Invoke no skill and launch no agent." and then contains:
   - the full content of [references/control.md](references/control.md), read with `Read` just before the call and pasted as is — not summarized from memory;
   - the **original version** and the **rewritten version**, set side by side;
   - the target reader identified at step 1, and the user's request quoted **verbatim** — the sub-agent does not see the conversation, and a paraphrase would carry the same misreading as the rewrite;
   - the **read-only** instruction: it modifies no file and proposes no replacement rewrite, it reports what is lost.

   Verdict `[PASS]` or `[FAIL]`. A verdict that is neither, or that contains both, counts as `[FAIL]`. A tool error relaunches the single check concerned, without consuming a pass.
   - On `[FAIL]`: fix and relaunch. Fixing a contested passage means **removing** what the check contests (the unestablished claim, the added word), not rephrasing it: a new wording often carries a new error, and a rewrite that says less but says it right passes. **2 passes maximum** — this sub-agent is a non-regression guard, not a style-improvement loop. Beyond that, leave the passage(s) concerned **in their original version** and say so in the closing block.
   - Skipped only when the target is **a single sentence** given inline. An inline paragraph is checked: nothing is written, but re-merging sentences is where a causal link the original did not give gets invented.
   - On a corpus: one sub-agent per file, launched in parallel in the same message.

6. **Present, then write after validation.** Render a before/after table, titled "proposed" (never "applied": nothing is written until the user has answered), one row per rewrite, with the named rule alongside. The "after" column contains **the exact text** proposed, in the language of the source — never a description of what it will say: the user can only arbitrate what they read. Below the table, a list **Questions to the author**, one line per missing link recorded at step 3 that was not restored, including in a passage left intact after the check failed (a rewrite attempted then withdrawn does not waive its question: the link is still missing) — none is omitted, even if it seems minor: it is for the reader of the original to say what the text does not say. Then `AskUserQuestion`: apply everything / apply a selection / apply nothing — **also on an inline target**, where the question is about which rewrites to keep. If the tool is not offered, ask the same question in text, right before the awaiting closing block. Settle that choice **before** composing the output (the tool is offered or it is not: a `ToolSearch` to find it happens upstream): a tool call between the output and the question splits the message in two, and only the last one is read. The message that carries the question therefore **itself** contains the diagnosis, the table, the questions to the author and the closing block; never write "the table above": if a tool was called after the output, copy everything back into the final message. **No file is written before the answer** — the user is the author of the text, a rewrite applied by default takes away the only arbitration that matters.

7. **Close** with one of the blocks below, at the end of the last message, once the check's verdict is back: never end the turn on a tool call. That last message carries **the whole** output of step 6 — diagnosis, before/after table, questions to the author, validation question, block — not the block alone: a message composed before the check is no longer read once the verdict is back.

## Invariants
What a rewrite never changes:

- **The meaning.** No information removed, added or qualified. Removing a hedge makes the assertion stronger — that is a change of meaning, not of form (Williams: the most common intensifier is the absence of a hedge). A connector is information: writing *thanks to*, *therefore* or *because* between two facts the original juxtaposed asserts a cause it did not give. When the antecedent or the link is missing from the source (what a cache caches, whose load drops), restore it with the words of the original only; otherwise, **report it as a question to the author** rather than guess it.
- **The designated responsibility.** Putting a character as subject, denominalizing or depassivizing shifts who is designated as responsible — Williams demonstrates it on an automobile recall letter, and ISO 5.1.6 forbids concealing content the reader needs to know. The shift may be desirable, but it is **reported** in the closing block, it is not done in silence.
- **The imposed vocabulary**: glossary terms, product names, code identifiers, quotes, figures, URLs. Non-intuitive corollary (GN3): **one concept, one word** — elegant variation forces the reader into a gratuitous bridge, so the instinct to avoid repetition (strong in French prose, Fowler's "elegant variation" in English) is a fault here, not a quality.
- **The Markdown structure**, the frontmatter, the link anchors, the heading levels.
- **No length target.** Never aim at a Flesch, Gunning Fog or SMOG score, nor at a number of words per sentence, nor cite them as justification. Do not quantify the sentence lengths of the text either ("3 to 6 words", "under 15 words") in the diagnosis: the defect is the cut link, never the word count. Cutting a sentence is forbidden when it forces a bridging inference (GN1, GN2); **lengthening is allowed** when it restores the old→new chain. The dependency locality theory says nothing against long sentences: it says something against long dependencies (G6).
- **What must stay complex stays complex.** Williams: *no simpler than they deserve, but no more difficult than they have to be*. A long sentence with short dependencies is good; a useful nominalization and a passive motivated by the flow are not defects.
- **Never a translation.**
- **On a source file, only the comments and docstrings are rewritten**, never the code — changing a line of code is not an editorial rework, and falls outside the mandate given.

## Output format
End with a block, in one of these four exact forms. `<n>` is a number (the number of rewrites that appear in the before/after table; at `0`, the message proposes applying no change) and the word that follows is `rewrite(s)`, never another unit ("paragraph", "sentences"); `<target>` names the target.

**As long as the user has not answered the question of step 6** — which is the case of the message that asks it, whether there is a file to write or not. Nothing is applied at this stage: never put `✅ [Rewrite applied]` there.
```
---
✍️ Rewrite — <n> rewrite(s) proposed on <target> · Check <✅ | ❌ | not required (single sentence)>
⏸️ [Rewrite awaiting validation]
---
```
With a check in `[FAIL]` after 2 passes, add `· left untouched: <passages>` on the `⏸️` line, including when no rewrite survived (`0 rewrite(s) proposed`): the `⚠️ [Rewrite partial]` block never comes in this message, only after the user's answer.

The next three forms close the message **that follows the user's answer**.

**If the check is `[PASS]`** (or was not required — single sentence inline):
```
---
✍️ Rewrite — <n> rewrite(s) on <target> · Check ✅
✅ [Rewrite applied]
---
```

**If the check stays `[FAIL]` after 2 passes**:
```
---
✍️ Rewrite — <n> rewrite(s) on <target> · Check ❌
⚠️ [Rewrite partial] — <summary of the last [FAIL]> · left untouched: <passages>
---
```

**If the user declines the rewrites**:
```
---
✍️ Rewrite — 🚫 [Rewrite not applied — declined by the user]
---
```

**In direct mode**, the only block, closing the single message that carries the rewritten text:
```
---
✍️ Rewrite — <n> rewrite(s) applied directly · Check <✅ | ❌>
---
```
With a check in `[FAIL]` after 2 passes, add `· left untouched: <passages>` on the same line.

In the awaiting form, the two applied forms and the direct form, add before the final `---` one line per detected shift:
`↪ Responsibility shift — <rule>: <actor now named, or now hidden>`

This block appears only when this skill has actually run: its absence directly signals that no diagnosis took place. Other skills (`/vibe:verify`, `/vibe:debrief`) may add their own block after this one.
