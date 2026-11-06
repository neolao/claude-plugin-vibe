import sqlite3

from flask import Blueprint, jsonify, request

from logistics.consignment import Parcel
from logistics.consignment_repository import ConsignmentRepository

bp = Blueprint("pickup", __name__)
repo = ConsignmentRepository(sqlite3.connect("dockside.db", check_same_thread=False))


# Called by the warehouse terminal when a packer scans a parcel onto the pallet.
@bp.post("/pickup-batches/<batch_id>/parcels")
def scan_parcel(batch_id: str):
    pickup_batch = repo.get(batch_id)
    pickup_batch.add_parcel(Parcel(request.json["parcel_id"], int(request.json["weight_grams"])))
    repo.save(pickup_batch)
    return jsonify({"batch_id": batch_id, "parcels": len(pickup_batch.parcels)})


# Called by the warehouse terminal when the driver arrives.
@bp.post("/pickup-batches/<batch_id>/close")
def close_batch(batch_id: str):
    pickup_batch = repo.get(batch_id)
    pickup_batch.close()
    repo.save(pickup_batch)
    return jsonify({"batch_id": batch_id, "status": pickup_batch.status})
