# Model of the `tasks.tsv` fallback

This file reproduces Claude Code's native task system (`TaskCreate`, `TaskUpdate`, `TaskList`, `TaskGet`) in a text file, one line per task. The operations are the same, with the same effects. The script `scripts/tasks.sh` applies them; the manual mode reproduces them by hand when the script cannot run.

## File
The file is `<scratchpad>/tasks.tsv`, or the one passed through the `file:` option (see "Input" in `SKILL.md`). Tab-separated columns, fixed first line:

```
# tasks v1	id	status	owner	blockedBy	subject	activeForm	description
1	completed		-	Write the parser	Writing the parser	Read contacts.csv as a stream.
2	in_progress		1	Write tests	Writing tests	Parser tests, including one invalid line.
3	pending	review-tests	2	Document the import	Documenting the import	README, ten lines.
```

| Column | Rule |
|---|---|
| `id` | Highest id in the file + 1 at creation. Never reused: a deleted task keeps its line. |
| `status` | `pending` \| `in_progress` \| `completed` \| `deleted`. A `deleted` line is skipped by `list`. |
| `owner` | Empty by default; name of the agent in charge of the task when there is one. |
| `blockedBy` | Ids of the tasks to complete before this one, comma-separated; `-` when there are none. |
| `subject` | Short title in the imperative. |
| `activeForm` | Progressive form of the subject, shown in the `●` line. |
| `description` | What has to be done and the completion criterion, on one line. |

- **`blocks` is not stored.** The tasks that `#2` blocks are those whose `blockedBy` contains `2`. A dependency therefore exists in one place only, and cannot be recorded on one side alone.
- No tab and no newline in a value: the script replaces them with spaces.
- No `metadata` field: the plugin does not use it.

## Operations
Each operation matches a native tool. Each entry gives the script call, then the manual equivalent.

### `create` ↔ `TaskCreate`
- Script: `tasks.sh <file> create --subject S --active-form A [--description D] [--blocked-by 1,2]` → `ok #<id> created`. The file and its header line are created on the first call.
- By hand: append a line `<highest id + 1>`, `pending`, empty owner, `blockedBy` (or `-`), subject, progressive form, description. If the file does not exist, write the header line first.

### `update` ↔ `TaskUpdate`
- Script: `tasks.sh <file> update <id> [--status S] [--subject S] [--active-form A] [--description D] [--owner O] [--add-blocked-by 1,2] [--add-blocks 4,5]` → `ok #<id> <status>`.
- By hand: edit the task's single line (`Edit`). `--add-blocks 4` applies to line `4`: add the task's id to its `blockedBy`. `deleted` also removes this id from the `blockedBy` of the other lines.

### `abandon` — no native equivalent
Used when a loop goes back to an earlier step (see "Going back" in `SKILL.md`): every `pending` task becomes stale at once.
- Script: `tasks.sh <file> abandon` → one `ok #<id> deleted` line per task deleted, or `(nothing to abandon)`. `in_progress` and `completed` tasks are untouched; each deleted id is removed from the other lines' `blockedBy`.
- By hand, and in native mode: one `deleted` transition per `pending` task (`TaskUpdate` or `Edit`), lowest id first.

### `list` ↔ `TaskList`
- Script: `tasks.sh <file> list`.
- By hand: reread the file and print the same summary, one line per non-deleted task:

```
#1 [completed] Write the parser
#2 [in_progress] Write tests
#3 [pending] Document the import (blockedBy: #2) · owner: review-tests
```

`blockedBy` only shows the tasks not yet `completed`; `owner` only appears when set.

### `get` ↔ `TaskGet`
- Script: `tasks.sh <file> get <id>`: every field, computed `blocks` included.
- By hand: reread the line and compute `blocks` as above.

## Refusals
The script refuses these operations (exit 1, `refused: …` on stderr, file unchanged). In manual mode, you forbid yourself the same ones:
- nonexistent or deleted id, dependency on itself;
- transition to `in_progress` while another task already is, or while a `blockedBy` is not `completed`;
- transition from `pending` to `completed` without `in_progress`.

Other exit codes: 2 = usage error (unknown option, invalid status), 3 = lock busy. During a write, the script locks the file with a `<file>.lock` directory. A lock left behind by an interruption can be removed by hand.
