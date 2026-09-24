import json


async def record(sink, kind: str, **fields) -> None:
    """Appends one line per manual stock change to the audit stream."""
    await sink.write(json.dumps({"kind": kind, **fields}) + "\n")
