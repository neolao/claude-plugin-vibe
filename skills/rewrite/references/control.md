# Rewrite Control Grid

## Mission
Compare an original version with its rewrite. The mandate is not to improve the style: it is to check that no information, no responsibility and no link was lost along the way, and that the gain in readability is real rather than cosmetic. A rewrite that reads better but says less is a failure, not a compromise.

## Control checklist
1. **Meaning preserved.** Does every piece of information of the original appear in the rewrite? Was nothing added that the original did not say? Check in particular the conditions, the exceptions, the reservations and the figures.
2. **Modality and ethos.** Are the hedges (*may, seems, often, most*) and the intensifiers (*proves, always, it is clear that*) at the same level? Removing a hedge makes the assertion stronger: that is a change of meaning, not of form.
3. **Designated responsibility.** Does the rewrite name an actor the original left silent, or hide an actor the original named? Putting a character as subject, denominalizing or depassivizing shifts who is designated as responsible. The shift may be legitimate — but it must be **reported**, never silent.
4. **Invariants.** Are glossary terms, product names, code identifiers, quotes, figures, URLs, Markdown structure, frontmatter and link anchors intact? Is the language the original's — no translation?
5. **No cut that forces a bridging inference.** For each sentence split or shortened: can the reader still attach the opening of the next sentence to a direct antecedent? A removed logical connector (*because, although, therefore*) that carried a relation counts as a loss of information, not as concision.
6. **Real, nameable gain.** Is each rewrite justified by an identified rule (`W*`, `GN*`, `G*`, `ISO 5.x`, `OUST-*`)? A rewrite whose only effect is to be shorter, or to "sound better", has no demonstrated gain.
7. **Over-correction.** Was the text flattened where the original was deliberately complex, indirect or nuanced? A useful nominalization kept, a passive motivated by the flow, a long sentence with short dependencies: these are not defects.

## Expected output
- `[PASS]` if the rewrite holds — only if every item of the checklist comes with cited proof (sentence of the original set side by side with the rewritten sentence); an item without cited proof counts as `[FAIL]`.
- `[FAIL]` + a bulleted list of the losses found otherwise, each located on the passage concerned and qualified: loss of information, unreported responsibility shift, broken invariant, bridge created, undemonstrated gain, or over-correction.

Read-only: modify no file, propose no replacement rewrite — only report what is lost.
