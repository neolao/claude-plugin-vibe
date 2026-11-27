import hashlib


async def store_trace(body):
    """Stores one diagnostic trace and returns its content id."""
    content_id = hashlib.sha256(body).hexdigest()
    await _blob_store.put(content_id, body)
    return content_id


class _BlobStore:
    async def put(self, key, value):
        raise NotImplementedError("bound at startup")


_blob_store = _BlobStore()
