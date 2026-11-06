import sqlite3

from flask import Blueprint, jsonify, request

from logistics.batch import Parcel
from logistics.batch_repository import BatchRepository

bp = Blueprint("pickup", __name__)
repo = BatchRepository(sqlite3.connect("dockside.db", check_same_thread=False))


# Called by the warehouse terminal when a packer scans a parcel onto the pallet.
@bp.post("/batches/<batch_id>/parcels")
def scan_parcel(batch_id: str):
    batch = repo.get(batch_id)
    batch.add_parcel(Parcel(request.json["parcel_id"], int(request.json["weight_grams"])))
    repo.save(batch)
    return jsonify({"batch_id": batch_id, "parcels": len(batch.parcels)})


# Called by the warehouse terminal when the driver arrives.
@bp.post("/batches/<batch_id>/close")
def close_batch(batch_id: str):
    batch = repo.get(batch_id)
    batch.close()
    repo.save(batch)
    return jsonify({"batch_id": batch_id, "status": batch.status})
