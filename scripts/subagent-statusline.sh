#!/bin/sh
set -eu
# Custom subagent panel rows — status icon, bold name, description, token count.
# Input: {..., "columns": N, "tasks": [{id,name,type,status,description,label,startTime,tokenCount,tokenSamples,cwd}, ...]}
# Output: one JSON line per row to override: {"id": "...", "content": "..."}

input=$(cat)

if ! output=$(printf '%s' "$input" | jq -c '
  (.columns // 60) as $columns |
  .tasks[]? |
  . as $task |
  ({
    completed: "[32m✓[0m",
    success: "[32m✓[0m",
    failed: "[31m✗[0m",
    error: "[31m✗[0m",
    running: "[33m▶[0m",
    in_progress: "[33m▶[0m"
  }[$task.status // "running"] // "[2m○[0m") as $icon |
  ($task.name // $task.label // "agent") as $name |
  ($task.tokenCount // 0) as $tokenCount |
  (($task.description // "") | gsub("\n"; " ")) as $desc |
  {id: $task.id, content: (($icon + " [1m" + $name + "[0m — " + $desc + " · " + ($tokenCount|tostring) + " tok")[0:$columns])}
' 2>&1); then
  echo "subagent-statusline: jq failed on hook input" >&2
  echo "$output" >&2
  exit 0
fi

echo "$output"
