"""Notes API handlers. Called by the web framework once per request."""

import json

from store import list_notes

PAGE_SIZE = 20


def get_notes(request):
    try:
        page = int(request.get("page", 1))
        notes = list_notes()
        start = page * PAGE_SIZE
        return {"status": 200, "body": json.dumps(notes[start:start + PAGE_SIZE])}
    except Exception as exc:
        return {"status": 500, "body": str(exc)}
