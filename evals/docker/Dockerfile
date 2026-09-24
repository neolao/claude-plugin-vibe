# Runs `claude plugin eval` in a Linux container.
# Used when the host cannot grant Bash to an eval: on a Mac with Docker Desktop,
# ~/.docker holds symlinks and the eval sandbox refuses every Bash-granting case.
# Usage: see evals/docker/README.md.
FROM node:22-bookworm-slim

# git: most skill cases commit. python3: tokens.py and Python fixtures.
# bubblewrap + socat: the Linux backend of the Bash sandbox.
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      git python3 jq bubblewrap socat ca-certificates curl ripgrep \
 && rm -rf /var/lib/apt/lists/*

ARG CLAUDE_CODE_VERSION=latest
RUN npm install -g "@anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}"

# The repo is mounted, not copied: its owner differs from the container user.
USER node
RUN git config --global user.name "vibe-eval" \
 && git config --global user.email "vibe-eval@localhost" \
 && git config --global init.defaultBranch main \
 && git config --global --add safe.directory '*'

WORKDIR /work
