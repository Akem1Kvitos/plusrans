from flask import Blueprint, current_app as app, Response

sources_api = Blueprint("sources_api", __name__)


@sources_api.route('/<file>', methods=["GET"])
def main_page(file: str):
    result = app.config.sources_service.get_source("", file)
    return Response(result['data'], mimetype=result['mimetype'])


@sources_api.route('/css/<file>', methods=['GET'])
def css(file: str):
    result = app.config.sources_service.get_source("css", file)
    return Response(result['data'], mimetype=result['mimetype'])


@sources_api.route('/js/<file>', methods=['GET'])
def js(file: str):
    result = app.config.sources_service.get_source("js", file)
    return Response(result['data'], mimetype=result['mimetype'])
