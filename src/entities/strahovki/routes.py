from flask import Blueprint, current_app as app, jsonify, request

strahovki_api = Blueprint("strahovki_api", __name__, url_prefix="/api/strahovki")


@strahovki_api.route("/", methods=["GET"])
def get_strahovki():
    result = app.config.strahovki_service.select()
    return jsonify(result), 200


@strahovki_api.route("/", methods=["POST"])
def add_strahovka():
    result = app.config.strahovki_service.insert(request.json)
    return jsonify(result), 200


@strahovki_api.route("/<int:field_id>", methods=["PUT"])
def update_strahovka(field_id: int):
    result = app.config.strahovki_service.update(field_id, request.json)
    return jsonify(result), 200


@strahovki_api.route('/<int:field_id>', methods=["DELETE"])
def delete_strahovka(field_id: int):
    result = app.config.strahovki_service.delete(field_id)
    return jsonify(result), 200
