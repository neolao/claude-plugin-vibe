#!/bin/sh
# Runs evals/tasks-script-test.sh under Linux, once per awk implementation:
#   mawk    — Debian / Ubuntu (default awk)
#   gawk    — Fedora, Arch, and Debian as soon as gawk is installed
#   busybox — Alpine and minimal images
# Usage: sh evals/tasks-script-linux.sh [mawk|gawk|busybox]…   (all by default)
# Exits 0 when every configuration passes. The images are pulled on the first call.
set -u

repo=$(cd "$(dirname "$0")/.." && pwd)
configs=${*:-mawk gawk busybox}
failed=''

for c in $configs; do
  case $c in
    mawk) image=debian:bookworm-slim prep=':' ;;
    gawk) image=debian:bookworm-slim prep='apt-get update -qq >/dev/null && apt-get install -y -qq gawk >/dev/null' ;;
    busybox) image=alpine:3 prep=':' ;;
    *) echo "unknown configuration: $c (mawk, gawk or busybox)" >&2; exit 2 ;;
  esac
  echo "=== $c ($image)"
  # The awk actually used is printed: an image that changed its default awk would show up here.
  out=$(docker run --rm -v "$repo:/work:ro" -w /work "$image" sh -c \
    "$prep && echo \"awk: \$(readlink -f \"\$(command -v awk)\")\" && sh evals/tasks-script-test.sh; echo \"exit=\$?\"" 2>&1)
  printf '%s\n' "$out" | grep -v '^ok '
  case $out in *"exit=0") ;; *) failed="$failed $c" ;; esac
done

echo
if [ -z "$failed" ]; then echo "All configurations pass: $configs"; else echo "Failed:$failed"; exit 1; fi
