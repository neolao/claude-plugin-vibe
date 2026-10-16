---
name: tasks
description: Creates and tracks a vibe workflow's task list and keeps it up to date until the end — through the native task system (TaskCreate / TaskUpdate / TaskList / TaskGet) when it is available, otherwise through a `tasks.tsv` file in the scratchpad, kept by a script that reproduces the same model (ids, statuses, blockedBy dependencies, owner). Invoked internally by other vibe skills, never directly by users.
argument-hint: "[file: <path>] then <one task per line: '<subject> ← blockedBy \"<other subject>\"' or '<subject> ← no dependency'>"
user-invocable: false
version: 2.0.0
model: claude-sonnet-5-5
---

# vibe:tasks — Task List Creation & Tracking

## Golden rule
A task list kept up to date at every transition, with the same model and the same rules whether the native task system is available or not. The fallback is not a degraded version: it is the same system, stored in a file.

## Input
- Invoked by another `vibe:*` skill, once per workflow run, right after that skill's plan is approved: `$ARGUMENTS` is the list to create, one task per line, subject ≤ 30 chars, each with its `blockedBy` dependency or `no dependency`.
- Loaded without a caller's list: split the requested work yourself into tasks of this format before creating them. Subject in the imperative ("Write tests"), `activeForm` in the progressive form ("Writing tests").
- Option `file: <path>`, on the first line of `$ARGUMENTS`, before the tasks: the list file in fallback mode. An absolute path is taken as is; a relative path is resolved from the scratchpad (`file: tasks-review.tsv` → `<scratchpad>/tasks-review.tsv`). Without this line, the file is `<scratchpad>/tasks.tsv`. Without a scratchpad indicated, a relative path resolves from the current working directory (see "Fallback file"). The script always receives the absolute path resolved this way, never the relative one. In native mode the option is ignored: say so before the first `TaskCreate`, with this sentence: "Option `file:` ignored: the native task system is available."
- If the list already exists (native: `TaskList` not empty; fallback: the chosen file is present), do not recreate it: append the new tasks to it.

## Detection
The native system is available if `TaskCreate` is in your tool list **or** if it loads through `ToolSearch` with the query `select:TaskCreate,TaskUpdate,TaskList,TaskGet`. A deferred tool is not a missing tool: conclude it is missing only after that `ToolSearch`. Detection happens once; the chosen mode holds for the whole session.

## Fallback file
The file is the one chosen at input (by default `tasks.tsv` in the scratchpad directory your system prompt indicates); the announcement quotes it as an absolute path. If your system prompt indicates no scratchpad and the path is not absolute (default or relative `file:`): ask for the location with **AskUserQuestion** (recommended option: the current working directory), never `/tmp` by default; if **AskUserQuestion** is not available, take the current working directory and append to the announcement "(no scratchpad indicated: path resolved from the current directory)".

## Create the tasks
**Native mode**: create every task in order with `TaskCreate` (`subject`, `description`, `activeForm`), then chain the dependencies with `TaskUpdate` (`addBlockedBy`) exactly as given. Finish by showing the list (`TaskList`).

**Fallback mode**: the native system is missing. Pick the mode: by the script if the Bash tool is in your tool list, by hand otherwise. Then run these steps in order, skipping none:
1. **Creation**, following the chosen mode below, then show the list (`list`).
2. **Announcement**, in visible text: the user does not read your reasoning, an announcement that only appears there has not been made. It opens the message of your first `●` line, right above it (if you already wrote it before the creation, do not repeat it):

   ```
   The native task system is not available in this environment — I track the tasks in `<absolute path of the file>`, with the same model, through the script.
   ● <activeForm of the first task>
   ```

   The sentence is copied word for word, without rephrasing, with the addition "(no scratchpad indicated: path resolved from the current directory)" when "Fallback file" requires it. In manual mode, replace "through the script" with "by hand (<reason>)".
3. **Reminder**: your final answer opens with the same sentence, addition included, word for word. That is where the user looks for the path of the list.

**Through the script**: every operation goes through `scripts/tasks.sh`, one Bash call per creation or transition. Its absolute path is the "Base directory for this skill" line shown at the top of this skill, followed by `/scripts/tasks.sh`. Always run it with `sh`, writing in full in every call the path of the script and the path of the file: never a shell variable (`F=… ; S=…`), which an allow rule `Bash(sh */skills/tasks/scripts/tasks.sh:*)` would not recognize:

```
sh <base>/scripts/tasks.sh <file> create --subject "…" --active-form "…" --description "…" [--blocked-by 1,2]
sh <base>/scripts/tasks.sh <file> update <id> --status in_progress|completed|pending|deleted [--owner …] [--add-blocked-by …] [--add-blocks …]
sh <base>/scripts/tasks.sh <file> list
sh <base>/scripts/tasks.sh <file> get <id>
```

Create the tasks in order: `create` returns `ok #<id> created`, and that id is the one you pass to `--blocked-by` for the next ones. The script refuses what the rules below forbid (exit 1, message `refused: …`, file unchanged). A refusal signals an error on your side: fix the sequence, for example move the task to `in_progress` before `completed`. Never work around a refusal by editing the file by hand. The details are in [references/model.md](references/model.md).

**By hand**: only if the script cannot run (no Bash, call refused, for example in a non-interactive session, or execution error). You then keep the same file yourself, following the manual operations of [references/model.md](references/model.md). Each transition edits a single line (`Edit`), and you enforce the script's refusals yourself.

## Rules, identical in both modes
1. Only one task `in_progress` at a time.
2. Move a task to `in_progress` **before** starting the work it describes, not after. Never `pending` to `completed` directly.
3. Do not start a task whose `blockedBy` is not `completed`.
4. Move to `completed` only when the work is entirely done. Failing tests, partial work, unresolved error: the task stays `in_progress` and you create a task for the blocker.
5. After each `completed`, reread the list (`TaskList` or `list`) and take the unblocked `pending` task with the lowest id.
6. A task that has become pointless goes `deleted`; it does not stay `pending` indefinitely.
7. A task discovered along the way is created the moment it appears, not reconstructed at the end.

## Standing instruction for the rest of this session
Once this skill has run, every status transition goes through `TaskUpdate` (native), through `tasks.sh update` (fallback, script) or through editing the task's line (fallback, by hand). Every transition comes with one compact status line in your reply:
- `● <activeForm>` on the transition to `in_progress`;
- `✓ <subject>` on the transition to `completed`, followed by ` — <concrete detail>` when one exists (commit hash, test count) — nothing restated.

The status line reports a transition already recorded, it does not replace it: the call comes first, the line second. This also holds for `in_progress`, even when the task fits in a single action. No transition is silent: a `completed` or an `in_progress` directly followed by another tool call, without its line in your message, is an error, even when several tasks follow each other (one `✓` line per completed task).

These lines are text of your reply: the user does not read your reasoning, a line that only appears there has not been written. Prose belongs in the final report, not in these lines. Do not re-invoke this skill for an update: this instruction covers them until the end of the session.

## Resume
After a `/compact`, an interruption or at the start of a new turn, reread the state before any action: `TaskList`, or `tasks.sh <file> list` (the whole file in manual mode). The file path is in the fallback announcement and in your final answers. Do not rely on what remains of the conversation: a `completed` task summarized by the compaction could be redone, an `in_progress` task forgotten.

## Separate lists
The skill does not know who calls it: a sub-agent shares the session's scratchpad, has no `TaskCreate` and receives no identifier of its own. Choosing a separate list is therefore up to the caller.
- The main agent uses the default file.
- An agent that wants a list of its own — a sub-agent, or an orchestrator that dedicates a list to a mission — passes `file:`.
- Without the option, two agents of the same session share `tasks.tsv`; avoiding that is up to the caller. The script locks the file during each write, so two agents sharing a list lose no write, but they mix their tasks.
- Never write in the file of a list you do not keep. You may read it if you are given its path; the `owner` field records the agent in charge of a task.
