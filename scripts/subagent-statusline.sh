#!/bin/sh
# Custom subagent panel rows — status icon, bold name, description, token count.
# Input: {..., "columns": N, "tasks": [{id,name,type,status,description,label,startTime,tokenCount,tokenSamples,cwd}, ...]}
# Output: one JSON line per row to override: {"id": "...", "content": "..."}

input=$(cat)

echo "$input" | jq -c '
  (.columns // 60) as $columns |
  .tasks[]? |
  . as $t |
  ($t.status // "running") as $status |
  (
    if $status == "completed" or $status == "success" then "[32m✓[0m"
    elif $status == "failed" or $status == "error" then "[31m✗[0m"
    elif $status == "running" or $status == "in_progress" then "[33m▶[0m"
    else "[2m○[0m"
    end
  ) as $icon |
  ($t.name // $t.label // "agent") as $name |
  ($t.tokenCount // 0) as $tok |
  (($t.description // "") | gsub("\n"; " ")) as $desc |
  ($icon + " [1m" + $name + "[0m — " + $desc + " · " + ($tok|tostring) + " tok") as $line |
  {id: $t.id, content: ($line[0:$columns])}
'
