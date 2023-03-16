from flask import Flask, jsonify
from mysql.connector import connect, Error

from src.app_config import AppConfig
from src.entities.base_index import index_page
from src.entities.exceptions import ServiceException
from src.entities.sources.routes import sources_api
from src.entities.sources.service import SourcesService
from src.entities.strahovki.routes import strahovki_api
from src.entities.strahovki.service import StrahovkiService
from src.entities.strahovki.template_views import strahovki_temp
from src.entities.tehosmotri.routes import tehosmotri_api
from src.entities.tehosmotri.service import TehosmotriService
from src.entities.tehosmotri.template_views import tehosmotri_temp
from src.entities.voditeli.routes import voditeli_api
from src.entities.voditeli.service import VoditeliService
from src.entities.voditeli.template_views import voditeli_temp


def __handle_exception(e: Exception):
    return jsonify({
        "code": 500,
        "message": str(e)
    }), 500


def __handle_service_exception(e: ServiceException):
    return jsonify({
        "code": e.code,
        "message": e.message
    }), e.code


def __create_database_connection(config: AppConfig) -> connect:
    try:
        connection = connect(
            host=config.db_host,
            port=config.db_port,
            user=config.db_user,
            password=config.db_pass,
            database=config.db_name)
    except Error as e:
        raise Exception(e)
    return connection


def init_blueprints(_app: Flask) -> None:
    _app.register_blueprint(sources_api)
    _app.register_blueprint(strahovki_api)
    _app.register_blueprint(tehosmotri_api)
    _app.register_blueprint(voditeli_api)
    _app.register_blueprint(voditeli_temp)
    _app.register_blueprint(strahovki_temp)
    _app.register_blueprint(tehosmotri_temp)
    _app.register_blueprint(index_page)


def init_services(_app: Flask, config: AppConfig) -> None:
    connection = __create_database_connection(config)

    _app.config.sources_service = SourcesService(config.views_path)
    _app.config.strahovki_service = StrahovkiService(connection)
    _app.config.tehosmotri_service = TehosmotriService(connection)
    _app.config.voditeli_service = VoditeliService(connection)


def init_exception_handler(_app: Flask) -> None:
    _app.register_error_handler(Exception, __handle_exception)
    _app.register_error_handler(ServiceException, __handle_service_exception)
