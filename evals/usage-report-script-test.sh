#!/bin/sh
# Test of the script skills/usage-report/scripts/usage-report.sh. Run by hand, from the repo root:
#   sh evals/usage-report-script-test.sh
# Exits 0 when everything passes, 1 otherwise. Only writes in a temporary directory.
set -u

here=$(cd "$(dirname "$0")" && pwd)
R="$here/../skills/usage-report/scripts/usage-report.sh"
dir=$(mktemp -d)
trap 'rm -rf "$dir"' EXIT
F="$dir/usage-report.tsv"
P="$dir/project"
mkdir -p "$P/.vibe"
fails=0

check() { # check <label> <expected> <actual>
  if [ "$2" = "$3" ]; then echo "ok   $1"; else
    echo "FAIL $1"; printf "     expected: %s\n     actual:   %s\n" "$2" "$3"; fails=$((fails + 1))
  fi
}
code() { "$@" >/dev/null 2>&1; echo $?; }

check "incr before init: refused" 1 "$(code sh "$R" "$F" incr rounds)"
check "init: unknown entry" 1 "$(code sh "$R" "$F" init review claude-x yes)"
check "init: invalid backlog flag" 2 "$(code sh "$R" "$F" init feature claude-x maybe)"
check "init" 0 "$(code sh "$R" "$F" init feature claude-sonnet-5-5 no)"
check "init: invalid model text" 1 "$(code sh "$R" "$F" init feature 'claude: 5' no)"
check "init twice overwrites" 0 "$(code sh "$R" "$F" init feature claude-sonnet-5-5 no)"
check "incr rounds" "ok rounds = 1" "$(sh "$R" "$F" incr rounds)"
check "incr rounds 2" "ok rounds = 3" "$(sh "$R" "$F" incr rounds 2)"
check "incr findings.low 4" "ok findings.low = 4" "$(sh "$R" "$F" incr findings.low 4)"
check "incr: unknown counter" 1 "$(code sh "$R" "$F" incr bugs)"
check "incr: invalid n" 2 "$(code sh "$R" "$F" incr rounds two)"
check "brick" "ok brick.findings-classifier = 1" "$(sh "$R" "$F" brick findings-classifier)"
check "brick again" "ok brick.findings-classifier = 2" "$(sh "$R" "$F" brick findings-classifier)"
check "brick: invalid name" 1 "$(code sh "$R" "$F" brick 'my project')"
check "write: no .vibe/" 1 "$(code sh "$R" "$F" write "$dir")"

out=$(sh "$R" "$F" write "$P")
check "write: file under .vibe/usage-reports/" "$P/.vibe/usage-reports" "$(dirname "$out")"
check "write: name" "feature.md" "$(basename "$out" | sed "s/^[0-9T-]*//")"
check "write: self-ignoring directory" "*" "$(cat "$P/.vibe/usage-reports/.gitignore")"
check "report: entry" "entry: feature" "$(grep '^entry:' "$out")"
check "report: backlog" "backlog: no" "$(grep '^backlog:' "$out")"
check "report: rounds" "rounds: 3" "$(grep '^rounds:' "$out")"
check "report: never-incremented counter at 0" "questions: 0" "$(grep '^questions:' "$out")"
check "report: brick" "  findings-classifier: 2" "$(grep 'findings-classifier' "$out")"
check "report: closed frontmatter" 2 "$(grep -c '^---$' "$out")"
check "write removes the counters" "absent" "$([ -e "$F" ] && echo present || echo absent)"
check "incr after write: refused" 1 "$(code sh "$R" "$F" incr rounds)"
printf 'node_modules/\n' > "$P/.vibe/usage-reports/.gitignore"
sh "$R" "$F" init fix claude-sonnet-5-5 yes >/dev/null; out2=$(sh "$R" "$F" write "$P")
check "write keeps an existing .gitignore and adds *" "node_modules/
*" "$(cat "$P/.vibe/usage-reports/.gitignore")"
check "write: a second run gets its own file" "fix.md" "$(basename "$out2" | sed "s/^[0-9T-]*//")"

# coordination: the counter keys live in KEYS and nowhere else may invent one
keys=$(sed -n "s/^KEYS='\(.*\)'$/\1/p" "$R")
for k in $keys; do
  check "SKILL.md table names $k" 1 "$(grep -c "incr $k" "$here/../skills/usage-report/SKILL.md" | awk '{print ($1 >= 1)}')"
done
for k in $(grep -o 'incr [a-z.]*' "$here/../skills/feature/workflow.md" | awk '{print $2}' | sort -u); do
  case " $keys " in *" $k "*) echo "ok   workflow.md counts a known key: $k" ;; *) echo "FAIL workflow.md counts an unknown key: $k"; fails=$((fails + 1)) ;; esac
done
for k in $(grep -o '`[a-z.]*` [≥>]' "$here/../scheduled-tasks/improve-skills-and-agents/SKILL.md" | tr -d '`' | awk '{print $1}' | sort -u); do
  case " $keys " in *" $k "*) echo "ok   routine reads a known key: $k" ;; *) echo "FAIL routine reads an unknown key: $k"; fails=$((fails + 1)) ;; esac
done

echo
if [ "$fails" -eq 0 ]; then echo "All tests pass."; else echo "$fails test(s) failed."; exit 1; fi
