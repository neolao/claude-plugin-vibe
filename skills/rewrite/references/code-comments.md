# Code Comments Grid

## Mission
Rework the **comments and docstrings** of a source file. The code is never touched: a badly chosen name or a magic constant may be reported as out of scope, never fixed here.

## Provenance
John Ousterhout, *A Philosophy of Software Design* — chapters 12 ("Why Write Comments? The Four Excuses"), 13 ("Comments Should Describe Things that Aren't Obvious from the Code"), 15 ("Write The Comments First") and 16 ("Modifying Existing Code"). Same numbering in the 1st and 2nd editions.

## The principle, and why it does not reduce to the slogan
> "The guiding principle for comments is that comments should describe things that aren't obvious from the code."

Two precisions that change the diagnosis:

- **"The code" means the code right next to the comment**, not the whole application. A comment does not have to avoid restating what is visible three files away.
- **"Obvious" is judged from the point of view of someone reading the code for the first time**, not the author's. If a reviewer says it is not obvious, it is not obvious — that is not up for debate.

The underlying reason: if the caller has to read a method's body to use it, **there is no abstraction left** — the method's whole complexity is exposed. The declaration alone is never enough: `substring(start, end)` says neither whether `end` is included, nor what happens when `start > end`.

## The real axis: the level of abstraction
The widespread slogan "comment the why, not the how" is not Ousterhout's position, and misses it on two points.

First, for him the **what** is on the right side: "The main goal of implementation comments is to help readers understand what the code is doing (not how it does it)." The *why* comes second, not first.

Second and above all, the real criterion is not the semantic category but the **distance in abstraction**:

> "Comments augment the code by providing information at a different level of detail. Some comments provide information at a lower, more detailed, level than the code […]. Other comments provide information at a higher, more abstract, level […]. **Comments at the same level as the code are likely to repeat the code.**"

So the question to ask in front of each comment is not "is this a what, a how or a why?" but **"at what level am I relative to the line next to me?"**. Same level = noise. Lower = precision (units, bounds, invariants). Higher = intent, framing, motivation.

To go one level up, three questions: *What is this code trying to do? What is the simplest thing you can say that explains everything in the code? What is the most important thing about this code?*

Secondary benefit of a good high-level comment: it **lets you judge the correctness of the code** — the reader can ask whether the code really does everything the comment announces.

## The four categories
| Type | Where | Contains | Does not contain |
|---|---|---|---|
| **Interface** | right before the declaration (class, method, function) | the abstraction provided, seen from the caller; each argument and the return value with their constraints; side effects; exceptions; preconditions; limitations (e.g. "single-threaded") | any implementation detail |
| **Data structure member** | next to the field declaration | what the variable **represents**; units; inclusive/exclusive bounds; the meaning of an allowed `null`; invariants; what the **absence** of an entry means | how the code manipulates it ("think nouns, not verbs") |
| **Implementation** | in the body, at the narrowest scope that covers the targeted code | what each major block does; what one loop iteration does; the non-deducible why | the line-by-line *how* |
| **Cross-module** | at an unavoidable crossing point, or in a central file that is referenced | the decision that crosses module boundaries, written **once** | duplication at every affected site |

Default coverage: **every class, every class variable and every method carries an interface comment.** The exception (trivial getter/setter) must be obvious — commenting everything costs less than debating each case. The first two categories are the most important.

---

## Rules

**OUST-1 — The comment can be reconstructed from the neighbouring code.**
*Symptom.* Apply Ousterhout's test: *could someone who has never seen this code write this comment by looking only at the code next to it?* If so, the comment adds nothing.
*Fix.* Delete it, **or** replace it with what was missing. Deleting is a valid, fully owned fix.
```java
// ✗
// Add a horizontal scroll bar
hScrollBar = new JScrollBar(JScrollBar.HORIZONTAL);
// ✓ (deletion: there was nothing to add)
hScrollBar = new JScrollBar(JScrollBar.HORIZONTAL);
```

**OUST-2 — The comment recycles the words of the name.**
*Symptom.* Remove from the comment the words present in the entity's name, its parameters and its types. If only function words remain, it fails.
*Fix.* "Use different words in the comment from those in the name of the entity being described." Explain the term itself, and add what the declaration does not say.
```java
// ✗
/* The horizontal padding of each line in the text. */
private static final int textHorizontalPadding = 4;
// ✓  (adds the unit, the fact that it applies on both sides, and paraphrases "padding")
/* The amount of blank space to leave on the left and right sides of each
 * line of text, in pixels. */
private static final int textHorizontalPadding = 4;
```

**OUST-3 — The comment sits at the same level of abstraction as the code.**
*Symptom.* About one comment per line; each phrase of the comment maps onto a token of the code; the comment paraphrases the operators and the tests.
*Fix.* Go one level up (intent) or one level down (precision). Never stay level.
```python
# ✗
ptr_copy = get_copy(obj)          # Get pointer copy
if is_unlocked(ptr_copy):         # Is obj free?
    return obj                    # return current obj
# ✓
# Fast path: an object nobody is copying is returned as-is.
ptr_copy = get_copy(obj)
if is_unlocked(ptr_copy):
    return obj
```

**OUST-4 — Variable declaration without precision.**
*Symptom.* The comment answers none of the five questions: units? inclusive or exclusive bounds? is `null` allowed, and what does it mean? who frees the resource? which invariants always hold? A specific case often forgotten: **what does the absence of an entry mean** in a collection?
*Fix.* Complete with **precision** — a level below the code.
```java
// ✗
// Contains all line-widths inside the document and number of appearances.
private TreeMap<Integer, Integer> lineWidths;
// ✓
// Holds statistics about line lengths of the form <length, count> where length
// is the number of characters in a line (including the newline), and count is
// the number of lines with exactly that many characters. If there are no lines
// with a particular length, then there is no entry for that length.
private TreeMap<Integer, Integer> numLinesWithLength;
```

**OUST-5 — Variable comment written in verbs.**
*Symptom.* The comment lists where and when the variable is modified (*Toggled to TRUE when… / Toggled to FALSE when…*): it traces the structure of the code instead of stating the meaning of the data.
*Fix.* "Think nouns, not verbs" — describe what the variable **represents**; the update rules become deducible again.

**OUST-6 — Long method without signposts, non-trivial loop without an iteration comment.**
*Symptom.* Several heterogeneous blocks chained without a marker; a loop of more than a few lines whose iteration invariant is not stated.
*Fix.* A more abstract comment before each major block; for a loop, say what **one** iteration does. Add nothing on short, obvious loops.
```c
// ✓
// Each iteration of the following loop extracts one request from the request
// message, increments the corresponding object, and appends a response.
for (i = 0; i < n; i++) { ... }
```

**OUST-7 — Undocumented public element.**
*Symptom.* Class, class variable or method without an interface comment.
*Fix.* Write one. The default rule is "everything".

**OUST-8 — Incomplete interface comment.**
*Symptom.* One of the five items is missing: behaviour as seen by the caller, each argument and the return value with their constraints and mutual dependencies, side effects, exceptions, preconditions.
*Fix.* Complete it — especially on the edge cases — so that the caller never needs to read the body to call the method.
```c
// ✗
/* Copy bytes out of the buffer. */
uint32_t Buffer::copy(uint32_t offset, uint32_t length, void* dest)
// ✓
/**
 * Copy a range of bytes from a buffer to an external location.
 * \param offset  Index within the buffer of the first byte to copy.
 * \param length  Number of bytes to copy.
 * \param dest    Where to copy the bytes: must have room for at least
 *                length bytes.
 * \return        The actual number of bytes copied, which may be less than
 *                length if the requested range extends past the end of the
 *                buffer. 0 if there is no overlap with the actual buffer.
 */
```

**OUST-9 — The implementation contaminates the interface.**
*Symptom.* The interface comment names private types, internal RPCs, private configuration parameters, an internal pattern — information the caller has no use for. Ousterhout: "one of the most common errors in interface comments".
*Fix.* Move that material **into** the body (implementation comment), and restate the interface in terms the caller can observe.

**OUST-10 — Cross-cutting decision undocumented, or documented twice.**
*Symptom.* Adding a variant requires touching N files and nothing says so; or the same decision is explained in three places that have drifted apart; or a comment before a call paraphrases the called method; or an external spec (HTTP, a file format) is reconstituted locally.
*Fix.* Document **once**, at the most obvious site, and point to it from the others (`// See "Zombies" in designNotes.`) — a broken pointer gets detected, a desynchronized duplicate does not. For external material: a URL or a one-sentence reference. Put the checklist where the developer will actually arrive.

**OUST-11 — The non-deducible "why" is absent, or lives in the commit message.**
*Symptom.* A hardware workaround, an imposed call order, a guard that looks dead, with no motivation. Or the motivation is in the commit: "a developer who needs the information is unlikely to think of scanning the repository log", and someone will undo the change and recreate the bug.
*Fix.* One line of motivation in the code; refer to the ticket rather than copying the bug report. Keeping it in the commit too is allowed — what matters is that it is in the code.
```java
// ✓
// The driver needs ~40ms to release the DMA buffer after close(); polling
// earlier returns stale data. Fixes RAM-436.
Thread.sleep(50);
```

**OUST-12 — Comment far from the code, or everything piled at the top.**
*Symptom.* A header block details three phases that take place forty lines further down.
*Fix.* Move each comment down to the narrowest scope that covers the targeted code; keep only an abstract strategy at the top. Dosage rule: **the farther a comment is from the code it describes, the more abstract it must be** — which is also what makes it cheaper to maintain.

---

## Counter-rules
What prevents over-correction, and what falls outside this skill's scope.

- **A long comment is not a writing defect.** Ousterhout has **no length metric**. When he fails to describe a method or a variable in a way that is both simple and complete, that is a red flag (*Hard to Describe*) about **the decomposition of the code**, not about the comment: "Comments serve as a canary in the coal mine of complexity." His rewrite of a variable comment runs five lines. **That diagnosis is reported, it is not fixed here** — refactoring is outside the mandate.
- **The most frequent defect is the opposite: the comment that is too vague.** *current*, *the data*, *handles the case* — the reader can deduce neither unit, nor reference point, nor domain. Complete with precision.
- **Density by elision, not by compression.** The criterion for a cut is "does the reader need it?", never "is it long?". A usage example that is not strictly necessary is kept if it has value of its own for a deep class.
- **Never touch the code.** A name that a long comment could replace, a magic constant, a shallow method: reported as out of scope, never modified.
- **The language of the source.** English comments stay English, and comments in any other language stay in that language, whatever language the exchange with the user is conducted in.
