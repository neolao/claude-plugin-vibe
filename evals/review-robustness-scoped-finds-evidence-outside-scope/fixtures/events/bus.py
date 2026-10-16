import json


async def publish(sink, topic: str, **fields) -> None:
    """Pushes one event to the dashboards' websocket sink."""
    await sink.send(json.dumps({"topic": topic, **fields}))
