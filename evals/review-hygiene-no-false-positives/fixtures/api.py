"""Public API of the `metrics` package - consumed by other services."""

__all__ = ["record_event", "flush"]

_buffer = []


def record_event(name, value):
    """Record a metric event. Called by other services that import this
    module; nothing inside this package calls it directly."""
    _buffer.append((name, value))


def flush(sink):
    """Flush buffered events to the given sink."""
    events, _buffer[:] = _buffer[:], []
    for name, value in events:
        sink.write(name, value)
