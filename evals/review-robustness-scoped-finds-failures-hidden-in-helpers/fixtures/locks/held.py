from contextlib import contextmanager


@contextmanager
def held(lock, timeout=5.0):
    if not lock.acquire(timeout=timeout):
        raise TimeoutError("lock busy")
    try:
        yield
    finally:
        lock.release()
