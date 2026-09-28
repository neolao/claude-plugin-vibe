def parse_users(text):
    rows = []
    for line in text.splitlines()[1:]:
        if not line.strip():
            continue
        user_id, name = line.split(",", 1)
        rows.append({"id": int(user_id), "name": name.strip().strip('"')})
    return rows
