from flask import jsonify, Blueprint

trips_routes_bp = Blueprint("tripes_routes",__name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"Ola": "mundo"}), 200

