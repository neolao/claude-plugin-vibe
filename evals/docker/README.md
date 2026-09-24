# Running evals in Docker

On a Mac with Docker Desktop, `~/.docker` holds symlinks (`cli-plugins/`,
`bin/lib/`). The eval sandbox then refuses every case that grants `Bash`:

> the Docker (~/.docker, DOCKER_CONFIG) credential store on this machine holds
> a symbolic link inside it … a Bash-granting evaluation cannot run here

The container has no `~/.docker`, so those cases run there. Cases without
`Bash` can still run on the host with the usual command.

## One-time setup

1. Docker Desktop running.
2. A long-lived token: run `claude setup-token` on the host and keep the
   token it prints. Never write it in a file of this repo.

The image builds itself on the first `run.sh` call. To rebuild it (new Claude
Code version): `docker build --no-cache -t vibe-eval evals/docker`.

## Running a case

From the repo root:

```bash
export CLAUDE_CODE_OAUTH_TOKEN=<token>   # or ANTHROPIC_API_KEY
evals/docker/run.sh <case-glob> [extra eval flags]
```

`run.sh` adds the canonical flags (`--scaffold --judge-model sonnet
--ablation none --keep-temp --trust-plugin --no-publish`). Pass the rest:
`--runs 1` for a validation run, and the case's `--allow-tools`.

```bash
evals/docker/run.sh review-tests-finds-violations --runs 1 --allow-tools Bash
```

It prints the eval table, then the `Tokens in/out` line of `tokens.py` for the
same run. The kept temp dirs live in the container's
`/tmp`, so `tokens.py` must run inside the same `docker run`: `run.sh` does
that. Results land in `evals/results/<timestamp>-<case>/` (gitignored).

## Notes

- `--security-opt seccomp=unconfined` is needed: the Bash sandbox uses
  bubblewrap, which needs user namespaces that Docker's default seccomp
  profile blocks.
- The repo is mounted at `/work`, not copied: edits on the host apply to the
  next run without rebuilding.
- The container runs Linux: a fixture that assumes macOS tools (BSD `sed`,
  `open`) behaves differently there.
