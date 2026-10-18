#!/bin/sh
# Test of the script skills/tasks/scripts/tasks.sh. Run by hand, from the repo root:
#   sh evals/tasks-script-test.sh
# Exits 0 when everything passes, 1 otherwise. Only writes in a temporary directory.
set -u

here=$(cd "$(dirname "$0")" && pwd)
T="$here/../skills/tasks/scripts/tasks.sh"
TAB=$(printf '\t')
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT
F="$dir/tasks.tsv"
fails=0

check() { # check <label> <expected> <actual>
  if [ "$2" = "$3" ]; then echo "ok   $1"; else
    echo "FAIL $1"; printf "     expected: %s\n     actual:   %s\n" "$2" "$3"; fails=$((fails + 1))
  fi
}
code() { "$@" >/dev/null 2>&1; echo $?; }
unchanged() { # unchanged <label> <command…>: refusal (exit 1) and identical file
  label=$1; shift
  before=$(cat "$F"); c=$(code "$@"); after=$(cat "$F")
  check "$label: exit 1" 1 "$c"
  check "$label: file unchanged" "$before" "$after"
}

# create / list / get
check "create #1" "ok #1 created" "$(sh "$T" "$F" create --subject 'Write the schema' --active-form 'Writing the schema' --description 'empty schema.sql')"
check "create #2 blocked by #1" "ok #2 created" "$(sh "$T" "$F" create --subject 'Write the migration' --active-form 'Writing the migration' --blocked-by 1)"
check "create #3" "ok #3 created" "$(sh "$T" "$F" create --subject 'Write tests' --active-form 'Writing tests')"
check "update #3 add-blocked-by 2" "ok #3 pending" "$(sh "$T" "$F" update 3 --add-blocked-by 2)"
check "v1 header" "# tasks v1" "$(head -n 1 "$F" | cut -f1)"
check "list" "#1 [pending] Write the schema
#2 [pending] Write the migration (blockedBy: #1)
#3 [pending] Write tests (blockedBy: #2)" "$(sh "$T" "$F" list)"
check "get #2: computed blocks" "blocks: #3" "$(sh "$T" "$F" get 2 | grep '^blocks')"
check "get #2: blockedBy" "blockedBy: #1" "$(sh "$T" "$F" get 2 | grep '^blockedBy')"

# refusals
unchanged "pending → completed directly" sh "$T" "$F" update 1 --status completed
unchanged "in_progress on a blocked task" sh "$T" "$F" update 2 --status in_progress
unchanged "dependency on a nonexistent id" sh "$T" "$F" update 2 --add-blocked-by 9
unchanged "dependency on itself" sh "$T" "$F" update 2 --add-blocked-by 2
unchanged "update of a nonexistent id" sh "$T" "$F" update 9 --status pending
check "in_progress #1" "ok #1 in_progress" "$(sh "$T" "$F" update 1 --status in_progress)"
check "create #4" "ok #4 created" "$(sh "$T" "$F" create --subject 'Document' --active-form 'Documenting')"
unchanged "two tasks in_progress" sh "$T" "$F" update 4 --status in_progress
check "completed #1" "ok #1 completed" "$(sh "$T" "$F" update 1 --status completed)"
check "#2 unblocked" "#2 [pending] Write the migration" "$(sh "$T" "$F" list | grep '^#2')"

# deleted: hidden, purged from dependencies, id never reused
check "add-blocks: #4 blocks #3" "ok #4 pending" "$(sh "$T" "$F" update 4 --add-blocks 3)"
check "#3 blocked by #2 and #4" "blockedBy: #2, #4" "$(sh "$T" "$F" get 3 | grep '^blockedBy')"
check "deleted #4" "ok #4 deleted" "$(sh "$T" "$F" update 4 --status deleted)"
check "#4 hidden by list" "" "$(sh "$T" "$F" list | grep '^#4')"
check "#4 purged from #3" "blockedBy: #2" "$(sh "$T" "$F" get 3 | grep '^blockedBy')"
unchanged "update of a deleted task" sh "$T" "$F" update 4 --status pending
check "id after deleted" "ok #5 created" "$(sh "$T" "$F" create --subject 'Clean up' --active-form 'Cleaning up')"

# texts: tab, newline, backslash, accents
tabbed=$(printf 'A\tB\nC \\n end')
sh "$T" "$F" update 5 --description "$tabbed" >/dev/null
check "tab and newline replaced" "description: A B C \\n end" "$(sh "$T" "$F" get 5 | grep '^description')"
check "7 columns per line" "7" "$(awk -F "$TAB" 'NR > 1 { print NF }' "$F" | sort -u)"
check "accents kept" "subject: Écrire le schéma" "$(sh "$T" "$F" update 5 --subject 'Écrire le schéma' >/dev/null; sh "$T" "$F" get 5 | grep '^#5' | sed 's/^#5 /subject: /')"
check "owner" "#5 [pending] Écrire le schéma · owner: review-tests" "$(sh "$T" "$F" update 5 --owner review-tests >/dev/null; sh "$T" "$F" list | grep '^#5')"

# usage and format
check "invalid status: exit 2" 2 "$(code sh "$T" "$F" update 5 --status finished)"
check "update without option: exit 2" 2 "$(code sh "$T" "$F" update 5)"
check "create without subject: exit 2" 2 "$(code sh "$T" "$F" create --active-form X)"
echo '{"nextId": 1}' > "$dir/old.json"
check "file in the wrong format: exit 1" 1 "$(code sh "$T" "$dir/old.json" list)"
check "missing file: empty list" "(no tasks)" "$(sh "$T" "$dir/missing.tsv" list)"

# concurrency: 20 parallel creations, no loss, unique ids
P="$dir/parallel.tsv"
i=1
while [ $i -le 20 ]; do sh "$T" "$P" create --subject "T$i" --active-form "T$i" >/dev/null & i=$((i + 1)); done
wait
check "20 parallel creations" "20" "$(awk 'NR > 1' "$P" | wc -l | tr -d ' ')"
check "unique ids" "20" "$(awk -F "$TAB" 'NR > 1 { print $1 }' "$P" | sort -u | wc -l | tr -d ' ')"
check "lock released" "absent" "$([ -e "$P.lock" ] && echo present || echo absent)"

# abandon: every pending task deleted, in_progress and completed kept, dependencies purged
A="$dir/abandon.tsv"
sh "$T" "$A" create --subject 'Plan' --active-form 'Planning' >/dev/null
sh "$T" "$A" create --subject 'Implement' --active-form 'Implementing' --blocked-by 1 >/dev/null
sh "$T" "$A" create --subject 'Review' --active-form 'Reviewing' --blocked-by 2 >/dev/null
sh "$T" "$A" create --subject 'Commit' --active-form 'Committing' --blocked-by 3 >/dev/null
sh "$T" "$A" update 1 --status in_progress >/dev/null && sh "$T" "$A" update 1 --status completed >/dev/null
sh "$T" "$A" update 2 --status in_progress >/dev/null && sh "$T" "$A" update 2 --status completed >/dev/null
check "in_progress #3" "ok #3 in_progress" "$(sh "$T" "$A" update 3 --status in_progress)"
check "abandon" "ok #4 deleted" "$(sh "$T" "$A" abandon)"
check "abandon keeps in_progress and completed" "#1 [completed] Plan
#2 [completed] Implement
#3 [in_progress] Review" "$(sh "$T" "$A" list)"
check "completed #3 after abandon" "ok #3 completed" "$(sh "$T" "$A" update 3 --status completed)"
check "abandon with nothing pending" "(nothing to abandon)" "$(sh "$T" "$A" abandon)"
check "abandon: extra argument" 2 "$(code sh "$T" "$A" abandon now)"
check "round 2 task after abandon" "ok #5 created" "$(sh "$T" "$A" create --subject 'Round 2 — Plan' --active-form 'Round 2 — Planning')"
check "round 2 chain" "ok #6 created" "$(sh "$T" "$A" create --subject 'Round 2 — Implement' --active-form 'Round 2 — Implementing' --blocked-by 5)"
check "abandon purges dependencies" "ok #5 deleted
ok #6 deleted" "$(sh "$T" "$A" abandon)"
check "#6 purged of #5" "blockedBy: -" "$(sh "$T" "$A" get 6 | grep '^blockedBy')"

echo
if [ "$fails" -eq 0 ]; then echo "All tests pass."; else echo "$fails test(s) failed."; exit 1; fi
