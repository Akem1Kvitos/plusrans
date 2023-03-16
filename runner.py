from dotenv import load_dotenv
from waitress import serve

from src.app import create_app
from src.app_config import AppConfig


def main():
    load_dotenv()
    config = AppConfig()
    app = create_app(config)
    serve(app, host="0.0.0.0", port=config.service_port, threads=config.workers)


if __name__ == "__main__":
    main()