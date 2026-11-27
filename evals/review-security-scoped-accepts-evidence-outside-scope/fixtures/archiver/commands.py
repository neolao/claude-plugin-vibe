import os
import tempfile
from datetime import date

from . import manifest, store, tokens
from .lib import ids, paths, perms, proc

DOCUMENTS_ROOT = "/srv/documents"
OUTBOX = "/srv/outbox"


def pack(user, folder):
    perms.require(user, "pack")
    dest = os.path.join(OUTBOX, f"{date.today():%Y%m%d}.tar.gz")
    proc.run_argv(["tar", "czf", dest, "-C", folder, "."])
    proc.run_tool("gpg", ["--batch", "--detach-sign", dest])
    return dest


def restore(user, archive_path):
    perms.require(user, "restore")
    job = ids.short_id()
    staging = tempfile.mkdtemp(prefix="restore-")
    proc.run_argv(["tar", "xzf", archive_path, "-C", staging])
    listing = manifest.read(staging)
    for entry in listing.entries:
        target = paths.inside(DOCUMENTS_ROOT, entry.name)
        store.copy(os.path.join(staging, "files", entry.name), target)
    index = store.load_index()
    index[listing.site] = len(listing.entries)
    store.save_index(index)
    return f"job {job}: {len(listing.entries)} documents restored"


def share(user, doc_id):
    perms.require(user, "share")
    token = tokens.share_token()
    store.save_share(doc_id, token, owner=user.name)
    return token


def rotate_key(user):
    perms.require(user, "rotate_key")
    key = tokens.api_key()
    store.save_api_key(user.name, key)
    return key
