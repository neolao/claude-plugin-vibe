"""Attachment downloads."""

from flask import Blueprint, send_file

from portal import storage

bp = Blueprint("files", __name__)


@bp.route("/files/<path:name>")
def download(name):
    """Serves a previously uploaded attachment to the requesting visitor."""
    return send_file(storage.upload_path(name))
