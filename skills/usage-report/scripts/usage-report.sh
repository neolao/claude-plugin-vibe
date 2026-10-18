#!/bin/sh
# Counters and writing of a workflow's usage report (see ../SKILL.md).
# POSIX sh + awk only: must run with macOS BWK awk as well as mawk, gawk and BusyBox awk.
#
#   usage-report.sh <counters> init <entry> <model> <backlog: yes|no>
#   usage-report.sh <counters> incr <key> [n]
#   usage-report.sh <counters> brick <name>
#   usage-report.sh <counters> show
#   usage-report.sh <counters> write <project root>
#
# init overwrites an existing counters file (one run = one init); write removes it once the
# report is on disk, so a run that stopped early never pollutes the next one.
# Exit: 0 = done, 1 = refused (file unchanged), 2 = usage error or write failure.
set -u

TAB=$(printf '\t')
ENTRIES='feature fix'
# Allowed counters: the report format must stay comparable from one report to the next.
KEYS='rounds questions fixes escalations returns.need returns.implementation findings.raised findings.dropped findings.merged findings.high findings.medium findings.low'

usage() {
  echo "usage: usage-report.sh <counters> init|incr|brick|show|write … (see the header of the script)" >&2
  exit 2
}
refuse() {
  echo "refused: $1" >&2
  exit 1
}

[ $# -ge 2 ] || usage
FILE=$1
CMD=$2
shift 2

is_int() { case $1 in '' | *[!0-9]*) return 1 ;; esac; }
in_list() { # in_list <word> <list>
  for w in $2; do [ "$w" = "$1" ] && return 0; done
  return 1
}
fail() { # fail <message>: an I/O failure, after cleaning the temp file
  rm -f "$FILE.tmp.$$"
  echo "error: $1" >&2
  exit 2
}
get() { awk -F "$TAB" -v k="$1" '$1 == k { v = $2 } END { print v }' "$FILE"; }
put() { # put <key> <value>: replace or append the line, through a temp file then mv
  tmp="$FILE.tmp.$$"
  awk -F "$TAB" -v OFS="$TAB" -v k="$1" -v v="$2" \
    '$1 == k { print k, v; done = 1; next } { print } END { if (!done) print k, v }' "$FILE" > "$tmp" && mv "$tmp" "$FILE" \
    || fail "could not write $FILE"
}

case $CMD in
  init)
    [ $# -eq 3 ] || usage
    in_list "$1" "$ENTRIES" || refuse "unknown entry: $1 (expected: $ENTRIES)"
    case $3 in yes | no) ;; *) usage ;; esac
    case $2 in '' | *[!a-z0-9.-]*) refuse "invalid model id: $2 (lowercase letters, digits, dots and dashes)" ;; esac
    mkdir -p "$(dirname "$FILE")" || fail "could not create $(dirname "$FILE")"
    tmp="$FILE.tmp.$$"
    {
      printf 'entry\t%s\n' "$1"
      printf 'model\t%s\n' "$2"
      printf 'backlog\t%s\n' "$3"
      printf 'start\t%s\n' "$(date +%s)"
    } > "$tmp" && mv "$tmp" "$FILE" || fail "could not write $FILE"
    echo "ok counters initialized: $FILE"
    ;;
  incr | brick)
    [ -s "$FILE" ] || refuse "$FILE missing: run init first"
    if [ "$CMD" = brick ]; then
      [ $# -eq 1 ] || usage
      case $1 in '' | *[!a-z0-9-]*) refuse "invalid brick name: $1" ;; esac
      key="brick.$1" n=1
    else
      [ $# -ge 1 ] && [ $# -le 2 ] || usage
      in_list "$1" "$KEYS" || refuse "unknown counter: $1 (expected: $KEYS)"
      key=$1 n=${2:-1}
      is_int "$n" || usage
    fi
    old=$(get "$key")
    put "$key" $(( ${old:-0} + n ))
    echo "ok $key = $(get "$key")"
    ;;
  show)
    [ $# -eq 0 ] || usage
    [ -s "$FILE" ] || refuse "$FILE missing"
    cat "$FILE"
    ;;
  write)
    [ $# -eq 1 ] || usage
    [ -s "$FILE" ] || refuse "$FILE missing"
    ROOT=$1
    [ -d "$ROOT/.vibe" ] || refuse "$ROOT has no .vibe/ directory (run /vibe:sync first)"
    entry=$(get entry)
    start=$(get start)
    now=$(date +%s)
    stamp=$(date +%Y-%m-%dT%H-%M-%S)
    in_list "$entry" "$ENTRIES" || refuse "$FILE has no valid entry: run init first"
    is_int "$start" || refuse "$FILE has no valid start: run init first"
    dir="$ROOT/.vibe/usage-reports"
    mkdir -p "$dir" || fail "could not create $dir"
    # The directory ignores itself: a report never reaches the project's history unless the user copies it out.
    grep -qx '\*' "$dir/.gitignore" 2>/dev/null || echo '*' >> "$dir/.gitignore" || fail "could not write $dir/.gitignore"
    out="$dir/$stamp-$entry.md"
    [ -e "$out" ] && refuse "$out already exists"
    tmp="$out.tmp.$$"
    {
      echo '---'
      echo "date: $(date +%Y-%m-%d)"
      echo "entry: $entry"
      echo "model: $(get model)"
      echo "backlog: $(get backlog)"
      echo "duration_minutes: $(( (now - start + 59) / 60 ))"
      for k in $KEYS; do v=$(get "$k"); echo "$k: ${v:-0}"; done
      echo 'bricks:'
      awk -F "$TAB" '$1 ~ /^brick\./ { sub(/^brick\./, "", $1); print "  " $1 ": " $2 }' "$FILE" | sort
      echo '---'
    } > "$tmp" && mv "$tmp" "$out" || { rm -f "$tmp"; fail "could not write $out"; }
    rm -f "$FILE"
    echo "$out"
    ;;
  *) usage ;;
esac
