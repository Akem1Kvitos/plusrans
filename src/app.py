import os

from flask import Flask

from src import init_blueprints, init_services, init_exception_handler
from src.app_config import AppConfig


def create_app(config: AppConfig) -> Flask:
    _app = Flask(__name__, template_folder='./templates')
    _app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    init_services(_app, config)
    init_blueprints(_app)
    init_exception_handler(_app)

    return _app
