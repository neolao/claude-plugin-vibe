#!/bin/sh
# Fallback operations of the `tasks` skill on a tasks.tsv file (see references/model.md).
# POSIX sh + awk only: must run with macOS BWK awk as well as mawk, gawk and BusyBox awk.
#
#   tasks.sh <file> create --subject S --active-form A [--description D] [--blocked-by 1,2]
#   tasks.sh <file> update <id> [--status S] [--subject S] [--active-form A] [--description D]
#                              [--owner O] [--add-blocked-by 1,2] [--add-blocks 4,5]
#   tasks.sh <file> abandon
#   tasks.sh <file> list
#   tasks.sh <file> get <id>
#
# Exit: 0 = done, 1 = refused (file unchanged), 2 = usage error, 3 = lock busy.
set -u

TAB=$(printf '\t')
HEADER="# tasks v1${TAB}id${TAB}status${TAB}owner${TAB}blockedBy${TAB}subject${TAB}activeForm${TAB}description"

usage() {
  echo "usage: tasks.sh <file> create|update|abandon|list|get … (see the header of the script)" >&2
  exit 2
}

[ $# -ge 2 ] || usage
FILE=$1
CMD=$2
shift 2

# A tab or a newline would break the format: replace them with spaces.
clean() { printf '%s' "$1" | tr '\t\r\n' '   '; }

is_id() { case $1 in '' | *[!0-9]*) return 1 ;; esac; }
is_ids() { case $1 in '' | ,* | *, | *,,* | *[!0-9,]*) return 1 ;; esac; }

# Values reach awk through the environment: `awk -v` would interpret backslashes.
T_ID='' T_STATUS='' T_SUBJECT='' T_ACTIVE='' T_DESC='' T_OWNER='' T_ADD_BY='' T_ADD_BLOCKS=''
T_SET_SUBJECT=0 T_SET_ACTIVE=0 T_SET_DESC=0 T_SET_OWNER=0

parse_flags() {
  while [ $# -gt 0 ]; do
    [ $# -ge 2 ] || usage
    case $1 in
      --subject) T_SUBJECT=$(clean "$2") T_SET_SUBJECT=1 ;;
      --active-form) T_ACTIVE=$(clean "$2") T_SET_ACTIVE=1 ;;
      --description) T_DESC=$(clean "$2") T_SET_DESC=1 ;;
      --owner) T_OWNER=$(clean "$2") T_SET_OWNER=1 ;;
      --status)
        case $2 in pending | in_progress | completed | deleted) T_STATUS=$2 ;; *) usage ;; esac ;;
      --blocked-by | --add-blocked-by) is_ids "$2" || usage; T_ADD_BY=$2 ;;
      --add-blocks) is_ids "$2" || usage; T_ADD_BLOCKS=$2 ;;
      *) usage ;;
    esac
    shift 2
  done
}

case $CMD in
  create)
    parse_flags "$@"
    [ "$T_SET_SUBJECT" = 1 ] && [ "$T_SET_ACTIVE" = 1 ] || usage
    [ -z "$T_STATUS$T_ADD_BLOCKS" ] && [ "$T_SET_OWNER" = 0 ] || usage
    ;;
  update)
    [ $# -ge 1 ] && is_id "$1" || usage
    T_ID=$1
    shift
    [ $# -ge 1 ] || usage
    parse_flags "$@"
    ;;
  get)
    [ $# -eq 1 ] && is_id "$1" || usage
    T_ID=$1
    ;;
  list | abandon) [ $# -eq 0 ] || usage ;;
  *) usage ;;
esac

if [ -s "$FILE" ]; then
  first=$(head -n 1 "$FILE")
  case $first in "# tasks v1"*) ;; *)
    echo "refused: $FILE is not a tasks v1 file" >&2
    exit 1
    ;;
  esac
fi

run_awk() { # run_awk <output file, empty for a read> <input file>
  out=$1
  shift
  T_MODE=$CMD T_ID=$T_ID T_STATUS=$T_STATUS T_SUBJECT=$T_SUBJECT T_ACTIVE=$T_ACTIVE \
    T_DESC=$T_DESC T_OWNER=$T_OWNER T_ADD_BY=$T_ADD_BY T_ADD_BLOCKS=$T_ADD_BLOCKS \
    T_SET_SUBJECT=$T_SET_SUBJECT T_SET_ACTIVE=$T_SET_ACTIVE T_SET_DESC=$T_SET_DESC \
    T_SET_OWNER=$T_SET_OWNER T_OUT=$out T_HEADER=$HEADER \
    awk -F "$TAB" '
function has(list, x,   a, n, i) {
  n = split(list, a, ",")
  for (i = 1; i <= n; i++) if (a[i] == x) return 1
  return 0
}
function add(list, x) {
  if (has(list, x)) return list
  return (list == "-" || list == "") ? x : list "," x
}
function drop(list, x,   a, n, i, r) {
  n = split(list, a, ",")
  r = ""
  for (i = 1; i <= n; i++) if (a[i] != x && a[i] != "-") r = (r == "") ? a[i] : r "," a[i]
  return (r == "") ? "-" : r
}
function refuse(msg) { print "refused: " msg > "/dev/stderr"; failed = 1; exit 1 }
function alive(x) { return (x in st) && st[x] != "deleted" }
function openDeps(x,   a, n, i, r) {
  n = split(by[x], a, ",")
  r = ""
  for (i = 1; i <= n; i++)
    if (a[i] != "-" && alive(a[i]) && st[a[i]] != "completed") r = (r == "") ? "#" a[i] : r ", #" a[i]
  return r
}
function blocksOf(x,   k, r) {
  r = ""
  for (k = 1; k <= count; k++)
    if (alive(ids[k]) && has(by[ids[k]], x)) r = (r == "") ? "#" ids[k] : r ", #" ids[k]
  return r
}
function checkDeps(list, self,   a, n, i) {
  n = split(list, a, ",")
  for (i = 1; i <= n; i++) {
    if (a[i] == self) refuse("a task cannot depend on itself (#" self ")")
    if (!alive(a[i])) refuse("task #" a[i] " does not exist")
  }
}
NR == 1 && /^# tasks v1/ { next }
NF == 0 { next }
{
  count++
  ids[count] = $1; st[$1] = $2; ow[$1] = $3; by[$1] = $4; su[$1] = $5; af[$1] = $6; de[$1] = $7
  if ($1 + 0 > maxId) maxId = $1 + 0
}
END {
  if (failed) exit 1
  m = ENVIRON["T_MODE"]; id = ENVIRON["T_ID"]

  if (m == "list") {
    shown = 0
    for (k = 1; k <= count; k++) {
      x = ids[k]
      if (st[x] == "deleted") continue
      line = "#" x " [" st[x] "] " su[x]
      d = openDeps(x); if (d != "") line = line " (blockedBy: " d ")"
      if (ow[x] != "") line = line " · owner: " ow[x]
      print line; shown++
    }
    if (!shown) print "(no tasks)"
    exit 0
  }

  if (m == "get") {
    if (!(id in st)) refuse("task #" id " does not exist")
    print "#" id " " su[id]
    print "status: " st[id]
    print "activeForm: " af[id]
    print "description: " de[id]
    print "owner: " (ow[id] == "" ? "-" : ow[id])
    b = by[id]; gsub(/,/, ", #", b); print "blockedBy: " (b == "-" ? "-" : "#" b)
    b = blocksOf(id); print "blocks: " (b == "" ? "-" : b)
    exit 0
  }

  if (m == "create") {
    id = maxId + 1
    deps = ENVIRON["T_ADD_BY"]
    if (deps != "") checkDeps(deps, id)
    count++; ids[count] = id
    st[id] = "pending"; ow[id] = ""; by[id] = (deps == "" ? "-" : deps)
    su[id] = ENVIRON["T_SUBJECT"]; af[id] = ENVIRON["T_ACTIVE"]; de[id] = ENVIRON["T_DESC"]
    msg = "ok #" id " created"
  }

  if (m == "update") {
    if (!(id in st)) refuse("task #" id " does not exist")
    if (st[id] == "deleted") refuse("task #" id " is deleted")
    deps = ENVIRON["T_ADD_BY"]
    if (deps != "") { checkDeps(deps, id); n = split(deps, a, ","); for (i = 1; i <= n; i++) by[id] = add(by[id], a[i]) }
    targets = ENVIRON["T_ADD_BLOCKS"]
    if (targets != "") { checkDeps(targets, id); n = split(targets, a, ","); for (i = 1; i <= n; i++) by[a[i]] = add(by[a[i]], id) }
    if (ENVIRON["T_SET_SUBJECT"] == 1) su[id] = ENVIRON["T_SUBJECT"]
    if (ENVIRON["T_SET_ACTIVE"] == 1) af[id] = ENVIRON["T_ACTIVE"]
    if (ENVIRON["T_SET_DESC"] == 1) de[id] = ENVIRON["T_DESC"]
    if (ENVIRON["T_SET_OWNER"] == 1) ow[id] = ENVIRON["T_OWNER"]
    s = ENVIRON["T_STATUS"]
    if (s == "in_progress" && st[id] != "in_progress") {
      for (k = 1; k <= count; k++) if (ids[k] != id && st[ids[k]] == "in_progress") refuse("#" ids[k] " is already in_progress, one task at a time")
      d = openDeps(id); if (d != "") refuse("#" id " is blocked by " d)
    }
    if (s == "completed" && st[id] == "pending") refuse("#" id " must go in_progress before completed")
    if (s == "deleted") for (k = 1; k <= count; k++) by[ids[k]] = drop(by[ids[k]], id)
    if (s != "") st[id] = s
    msg = "ok #" id " " st[id]
  }

  # abandon: every pending task goes deleted (a loop went back to an earlier step).
  # in_progress and completed tasks are kept: they are the trace of the round that happened.
  if (m == "abandon") {
    msg = ""
    for (k = 1; k <= count; k++) {
      x = ids[k]
      if (st[x] != "pending") continue
      st[x] = "deleted"
      for (j = 1; j <= count; j++) by[ids[j]] = drop(by[ids[j]], x)
      msg = (msg == "") ? "ok #" x " deleted" : msg "\nok #" x " deleted"
    }
    if (msg == "") msg = "(nothing to abandon)"
  }

  out = ENVIRON["T_OUT"]
  print ENVIRON["T_HEADER"] > out
  for (k = 1; k <= count; k++) {
    x = ids[k]
    print x "\t" st[x] "\t" ow[x] "\t" by[x] "\t" su[x] "\t" af[x] "\t" de[x] > out
  }
  close(out)
  print msg
}' "$@"
}

case $CMD in
  list | get)
    if [ -s "$FILE" ]; then run_awk "" "$FILE"; else run_awk "" /dev/null; fi
    exit $?
    ;;
esac

# Write: lock by mkdir (atomic, portable; flock does not exist on macOS),
# then a temporary file in the same directory and mv, so a reader never sees a half-written file.
mkdir -p "$(dirname "$FILE")" || exit 2
LOCK="$FILE.lock"
tries=0
until mkdir "$LOCK" 2>/dev/null; do
  tries=$((tries + 1))
  if [ "$tries" -ge 50 ]; then
    echo "error: lock $LOCK busy (remove it if it is orphaned)" >&2
    exit 3
  fi
  sleep 0.1
done
TMP="$FILE.tmp.$$"
trap 'rm -f "$TMP"; rmdir "$LOCK" 2>/dev/null' EXIT
trap 'exit 130' INT TERM

if [ -s "$FILE" ]; then run_awk "$TMP" "$FILE"; else run_awk "$TMP" /dev/null; fi
status=$?
[ "$status" -eq 0 ] || exit "$status"
mv "$TMP" "$FILE"
