#!/bin/sh
# Replays the CURRENT eval case of a skill/agent on its past versions (git),
# and stores the result in evals/history/timeline.json.
#
#   collect.sh <skill|agent> <cas> [--dry-run] [--refresh] [--max N]
#
# One point = one distinct state of the skill/agent (key: version + model), at the
# latest commit of that state. --refresh only reruns the points whose case changed
# since they were measured. See CLAUDE.md, "Evolution history".
set -eu

ROOT=$(cd "$(dirname "$0")/../.." && pwd)
HIST="$ROOT/evals/history"
TL="$HIST/timeline.json"
usage() { echo "usage: $0 <skill|agent> <cas> [--dry-run] [--refresh] [--max N]" >&2; exit 2; }

[ $# -ge 2 ] || usage
ITEM=$1; CASE=$2; shift 2
DRY=0; REFRESH=0; MAX=0
while [ $# -gt 0 ]; do
  case $1 in
    --dry-run) DRY=1 ;;
    --refresh) REFRESH=1 ;;
    --max) shift; MAX=$1 ;;
    *) usage ;;
  esac
  shift
done

cd "$ROOT"
[ -d "evals/$CASE" ] || { echo "unknown case : evals/$CASE" >&2; exit 1; }
command -v jq >/dev/null || { echo "jq required" >&2; exit 1; }

if [ -f "agents/$ITEM.md" ]; then KIND=agent; SPATH="agents/$ITEM.md"
elif [ -d "skills/$ITEM" ]; then KIND=skill; SPATH="skills/$ITEM"
else echo "neither agents/$ITEM.md nor skills/$ITEM" >&2; exit 1; fi

# A case that grants Bash runs in Docker (the host sandbox refuses it), mounting the commit's worktree.
USE_DOCKER=0
if grep -Eq '^allowed_tools:.*Bash' "evals/$CASE/prompt.md"; then
  USE_DOCKER=1
  if [ "$DRY" = 0 ] && [ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}${ANTHROPIC_API_KEY:-}" ]; then
    echo "Bash case: CLAUDE_CODE_OAUTH_TOKEN (or ANTHROPIC_API_KEY) required, see evals/docker/README.md (zsh -ic)" >&2; exit 1
  fi
fi

# Operator grants the case needs (see CLAUDE.md, "Agent model evals").
GRANTS=$(sed -n 's/^allowed_tools:.*\[\(.*\)\].*/\1/p' "evals/$CASE/prompt.md" | tr ',' '\n' | tr -d ' ' | grep -E '^(Bash|Write|Edit|ToolSearch|WebFetch)$' | tr '\n' ' ' || true)

# Case fingerprint: content of evals/<case>/ (prompt, graders, case.yaml, scaffold).
case_hash() {
  (cd "$1/evals/$CASE" && find . -type f | LC_ALL=C sort | xargs shasum | shasum | cut -c1-12)
}
CUR_HASH=$(case_hash "$ROOT")

[ -f "$TL" ] || echo '[]' > "$TL"

# State key of a skill/agent at a commit: version + model.
state_key() {
  f=$1
  [ "$KIND" = skill ] && f="$SPATH/SKILL.md"
  git show "$2:$f" 2>/dev/null | awk '
    /^version:/ && !v {v=$2} /^model:/ && !m {m=$2} END {print (v?v:"none") "|" (m?m:"-")}'
}

# Points: oldest to newest, last commit of each consecutive state.
POINTS=$(git log --reverse --format='%h %cs' -- "$SPATH" | while read -r sha date; do
  echo "$sha $date $(state_key "$SPATH" "$sha")"
done | awk '{ if ($3 != prev && NR > 1) print last; last=$0; prev=$3 } END { print last }')
[ "$MAX" -gt 0 ] && POINTS=$(echo "$POINTS" | tail -n "$MAX")

echo "$KIND $ITEM, cas $CASE (empreinte $CUR_HASH)"
echo "$POINTS" | while read -r sha date key; do
  ver=${key%%|*}; model=${key#*|}
  old=$(jq -r --arg i "$ITEM" --arg c "$CASE" --arg s "$sha" \
    '[.[]|select(.item==$i and .case==$c and .sha==$s)][0].caseHash // ""' "$TL")
  if [ -n "$old" ] && { [ "$REFRESH" = 0 ] || [ "$old" = "$CUR_HASH" ]; }; then
    echo "  $sha $date v$ver : already measured ($old), skipped"; continue
  fi
  echo "  $sha $date v$ver model=$model : to measure"
  [ "$DRY" = 1 ] && continue

  WT=$(mktemp -d "${TMPDIR:-/tmp}/neolao-hist.XXXXXX")
  git worktree add --detach "$WT/w" "$sha" >/dev/null 2>&1
  rm -rf "$WT/w/evals" && cp -R "$ROOT/evals" "$WT/w/evals"
  OUT="$ROOT/evals/results/history/$ITEM/$CASE/$sha"
  rm -rf "$OUT"; mkdir -p "$OUT"
  if [ "$USE_DOCKER" = 1 ]; then
    docker image inspect vibe-eval >/dev/null 2>&1 || docker build -t vibe-eval "$ROOT/evals/docker"
    docker run --rm --security-opt seccomp=unconfined --security-opt systempaths=unconfined \
      -e CLAUDE_CODE_OAUTH_TOKEN -e ANTHROPIC_API_KEY -v "$WT/w:/work" -v "$OUT:/out" vibe-eval \
      bash -c "claude plugin eval . --case '$CASE' --scaffold --judge-model sonnet --ablation none \
        --trust-plugin --no-publish --runs 3 --output-dir /out ${GRANTS:+--allow-tools $GRANTS}" \
      > "$OUT/eval.log" 2>&1 || echo "    non-zero exit code (case below threshold, or error), see $OUT/eval.log"
  else
    ( cd "$WT/w" && CLAUDE_CODE_WALNUT_SPIRE=1 claude plugin eval . --case "$CASE" \
        --scaffold --ablation none --runs 3 --judge-model sonnet --no-publish \
        --output-dir "$OUT" ${GRANTS:+--allow-tools $GRANTS} ) > "$OUT/eval.log" 2>&1 \
      || echo "    non-zero exit code (case below threshold, or error), see $OUT/eval.log"
  fi
  git worktree remove --force "$WT/w"; rm -rf "$WT"

  AGG="$OUT/aggregate-result.json"
  if [ ! -f "$AGG" ]; then echo "    no result for $sha" >&2; continue; fi
  jq --arg i "$ITEM" --arg k "$KIND" --arg c "$CASE" --arg s "$sha" --arg d "$date" \
     --arg v "$ver" --arg m "$model" --arg h "$CUR_HASH" --arg r "$(date +%F)" --slurpfile a "$AGG" '
    map(select(.item==$i and .case==$c and .sha==$s | not)) + [{
      item:$i, kind:$k, case:$c, sha:$s, date:$d, version:$v, model:$m, caseHash:$h, runAt:$r,
      score:$a[0].aggregates.overallScore, passRate:$a[0].aggregates.overallPassRate,
      cost:$a[0].costUsd }]' "$TL" > "$TL.tmp" && mv "$TL.tmp" "$TL"
  echo "    score $(jq -r --arg i "$ITEM" --arg c "$CASE" --arg s "$sha" '[.[]|select(.item==$i and .case==$c and .sha==$s)][0]|"\(.score) (\(.passRate)) \(.cost)$"' "$TL")"
done

# Current fingerprints of all tracked cases + data for the page (file:// without fetch).
jq -r '[.[].case]|unique[]' "$TL" | while read -r c; do
  h=$( (cd "$ROOT/evals/$c" && find . -type f | LC_ALL=C sort | xargs shasum | shasum | cut -c1-12) )
  ch=$(git log -1 --format=%cs -- "evals/$c" 2>/dev/null || true)
  jq -n --arg c "$c" --arg h "$h" --arg d "${ch:-}" '{($c):{hash:$h,lastCommit:$d}}'
done | jq -s 'add // {}' > "$HIST/cases.json"
# Data embedded in the page (/*DATA*/ … /*END*/ markers): works over file://, no external load.
DATA="window.TIMELINE=$(jq -c . "$TL");window.CASES=$(jq -c . "$HIST/cases.json");"
awk -v d="$DATA" '/\/\*DATA\*\//{print; print d; skip=1; next} /\/\*END\*\//{skip=0} !skip' "$HIST/index.html" > "$HIST/index.html.tmp" && mv "$HIST/index.html.tmp" "$HIST/index.html"
