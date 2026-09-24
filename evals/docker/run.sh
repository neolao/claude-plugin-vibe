#!/usr/bin/env bash
# Runs one eval in the container, then tokens.py on the same run.
# Usage: evals/docker/run.sh <case-glob> [extra `claude plugin eval` flags...]
# Example: evals/docker/run.sh feature-blocks-commit-on-failing-build --runs 1 --allow-tools Bash Write Edit
set -euo pipefail

case_glob="${1:?usage: run.sh <case-glob> [eval flags...]}"
shift

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
image="vibe-eval"

if [ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  echo "run.sh: set CLAUDE_CODE_OAUTH_TOKEN (from \`claude setup-token\`) or ANTHROPIC_API_KEY" >&2
  exit 1
fi

docker image inspect "$image" >/dev/null 2>&1 \
  || docker build -t "$image" "$repo/evals/docker"

out="evals/results/$(date +%Y%m%d-%H%M%S)-${case_glob//[^A-Za-z0-9_-]/_}"

# seccomp=unconfined: bubblewrap needs user namespaces, which Docker's default
# seccomp profile blocks. systempaths=unconfined: without it, bubblewrap cannot
# mount /proc in its sandbox ("Can't mount proc on /newroot/proc"). The
# container itself is the isolation boundary.
docker run --rm \
  --security-opt seccomp=unconfined \
  --security-opt systempaths=unconfined \
  -e CLAUDE_CODE_OAUTH_TOKEN -e ANTHROPIC_API_KEY \
  -v "$repo:/work" \
  "$image" \
  bash -c '
    set -uo pipefail
    out="$1"; case_glob="$2"; shift 2
    claude plugin eval . --case "$case_glob" --scaffold --judge-model sonnet \
      --ablation none --keep-temp --trust-plugin --no-publish \
      --output-dir "$out" "$@"
    status=$?
    # No --cleanup: kept dirs die with the container (--rm).
    python3 evals/tokens.py "$out"
    exit $status
  ' _ "$out" "$case_glob" "$@"
