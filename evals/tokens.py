#!/usr/bin/env python3
"""Reports the tokens of a `claude plugin eval` run launched with --keep-temp.

Usage: python3 evals/tokens.py <output-dir> [--cleanup]

<output-dir> is the --output-dir passed to `claude plugin eval`. The script reads
aggregate-result.json there, which gives each run's exact trace path: no
directory is guessed by glob. The `result` line of each trace carries
`modelUsage`, which breaks down every model of the session — main agent and
sub-agents included — with the cost of each.

Before printing anything, the count is reconciled with the CLI's cost:
  Σ costUSD of modelUsage   == total_cost_usd of the result line
  total_cost_usd + judgeCostUsd == the run's costUsd in aggregate-result.json
A mismatch, a missing trace (--keep-temp forgotten) or a missing result line
(interrupted run) stops the script with an error, rather than producing a
wrong or incomplete number.

  in  = inputTokens + cacheCreationInputTokens + cacheReadInputTokens
  out = outputTokens (thinking included, as in billing)

The judge is not counted: its tokens are written nowhere, only its cost is
(judgeCostUsd). The Cost column of history.md includes it, the Tokens column
does not.

--cleanup deletes, after a successful reconciliation, exactly the temporary
directories of the runs read — never a global /private/tmp/e-*, which could
belong to another run in progress.
"""

import json
import os
import shutil
import sys

EPSILON = 1e-6


def fail(message):
    sys.exit(f"tokens.py: {message}")


def fmt(n):
    return f"{n:,}".replace(",", " ")


def result_line(trace_path):
    for line in open(trace_path):
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if record.get("type") == "result":
            return record
    return None


def measure_run(label, run):
    trace = run.get("tracePath")
    if not trace or not os.path.exists(trace):
        fail(f"{label}: missing trace ({trace}). Was the run launched with --keep-temp?")
    result = result_line(trace)
    if result is None:
        fail(f"{label}: no `result` line in {trace}. Interrupted run?")
    models = result.get("modelUsage") or {}
    if not models:
        fail(f"{label}: `result` line without modelUsage in {trace}.")

    tokens_in = tokens_out = 0
    models_cost = 0.0
    for usage in models.values():
        tokens_in += (usage.get("inputTokens", 0)
                      + usage.get("cacheCreationInputTokens", 0)
                      + usage.get("cacheReadInputTokens", 0))
        tokens_out += usage.get("outputTokens", 0)
        models_cost += usage.get("costUSD", 0.0)

    session_cost = result.get("total_cost_usd", 0.0)
    if abs(models_cost - session_cost) > EPSILON:
        fail(f"{label}: Σ costUSD of modelUsage ({models_cost}) ≠ total_cost_usd ({session_cost}).")
    run_cost = run.get("costUsd", 0.0)
    judge_cost = run.get("judgeCostUsd", 0.0) or 0.0
    if abs(session_cost + judge_cost - run_cost) > EPSILON:
        fail(f"{label}: total_cost_usd + judgeCostUsd ({session_cost + judge_cost}) "
             f"≠ the run's costUsd ({run_cost}). The count does not cover the whole run.")

    return tokens_in, tokens_out, sorted(models), os.path.dirname(os.path.dirname(trace))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    cleanup = "--cleanup" in sys.argv[1:]
    if len(args) != 1:
        fail("usage: python3 evals/tokens.py <output-dir> [--cleanup]")
    aggregate = os.path.join(args[0], "aggregate-result.json")
    if not os.path.exists(aggregate):
        fail(f"{aggregate} not found. Is --output-dir the same as the run's?")

    temp_dirs = []
    for case in json.load(open(aggregate))["cases"]:
        for arm, runs in case["arms"].items():
            total_in = total_out = 0
            models = set()
            for i, run in enumerate(runs, 1):
                tokens_in, tokens_out, run_models, temp_dir = measure_run(
                    f"{case['name']} [{arm}] run {i}", run)
                total_in += tokens_in
                total_out += tokens_out
                models.update(run_models)
                temp_dirs.append(temp_dir)
            print(f"{case['name']} [{arm}] — {len(runs)} run(s), models: {', '.join(sorted(models))}")
            print(f"  Tokens in/out: {fmt(total_in)} / {fmt(total_out)}")

    if cleanup:
        for temp_dir in temp_dirs:
            if not os.path.basename(temp_dir).startswith("e-"):
                fail(f"refusing to delete {temp_dir}: not an eval temporary directory.")
            for root, dirs, _ in os.walk(temp_dir):
                for d in dirs:
                    os.chmod(os.path.join(root, d), 0o700)
            os.chmod(temp_dir, 0o700)
            shutil.rmtree(temp_dir)
        print(f"  {len(temp_dirs)} temporary director(ies) deleted.")


if __name__ == "__main__":
    main()
