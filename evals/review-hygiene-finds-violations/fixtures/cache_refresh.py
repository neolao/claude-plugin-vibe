def refresh_cache(store):
    # TODO: handle the case where store is empty
    entries = store.fetch_all()
    return {entry.id: entry for entry in entries}
