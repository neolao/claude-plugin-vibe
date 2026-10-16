import json
import queue

_outbox: "queue.Queue[str]" = queue.Queue()


def publish(topic: str, **fields) -> None:
    """Queues one event for the dashboards; the websocket task drains the queue."""
    _outbox.put_nowait(json.dumps({"topic": topic, **fields}))


def drain():
    while True:
        try:
            yield _outbox.get_nowait()
        except queue.Empty:
            return
