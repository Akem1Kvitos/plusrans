from flask import Blueprint, current_app as app, jsonify, request

voditeli_api = Blueprint("voditeli_api", __name__, url_prefix="/api/voditeli")


@voditeli_api.route("/", methods=["GET"])
def get_voditeli():
    result = app.config.voditeli_service.select()
    return jsonify(result), 200


@voditeli_api.route("/", methods=["POST"])
def add_voditeli():
    result = app.config.voditeli_service.insert(request.json)
    return jsonify(result), 200


@voditeli_api.route("/<int:field_id>", methods=["PUT"])
def update_voditeli(field_id: int):
    result = app.config.voditeli_service.update(field_id, request.json)
    return jsonify(result), 200


@voditeli_api.route('/<int:field_id>', methods=["DELETE"])
def delete_voditeli(field_id: int):
    result = app.config.voditeli_service.delete(field_id)
    return jsonify(result), 200
