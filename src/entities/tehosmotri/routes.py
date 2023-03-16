from flask import Blueprint, current_app as app, jsonify, request

tehosmotri_api = Blueprint("tehosmotri_api", __name__, url_prefix="/api/tehosmotri")


@tehosmotri_api.route("/", methods=["GET"])
def get_tehosmotri():
    result = app.config.tehosmotri_service.select()
    return jsonify(result), 200


@tehosmotri_api.route("/", methods=["POST"])
def add_tehosmotri():
    result = app.config.tehosmotri_service.insert(request.json)
    return jsonify(result), 200


@tehosmotri_api.route("/<int:field_id>", methods=["PUT"])
def update_tehosmotri(field_id: int):
    result = app.config.tehosmotri_service.update(field_id, request.json)
    return jsonify(result), 200


@tehosmotri_api.route('/<int:field_id>', methods=["DELETE"])
def delete_tehosmotri(field_id: int):
    result = app.config.tehosmotri_service.delete(field_id)
    return jsonify(result), 200