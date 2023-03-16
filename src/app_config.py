import os

SERVICE_PORT = "SERVICE_PORT"
SERVICE_WORKERS = "SERVICE_WORKERS"
DB_HOST = "DB_HOST"
DB_PORT = "DB_PORT"
DB_USER = "DB_USER"
DB_PASSWORD = "DB_PASSWORD"
DB_NAME = "DB_NAME"
SERVICE_VIEWS_PATH = "SERVICE_VIEWS_PATH"


class AppConfig:
    def __init__(self):
        self.service_port = int(os.getenv(SERVICE_PORT, default=8080))
        self.workers = os.getenv(SERVICE_WORKERS, default=3)

        self.views_path = os.getenv(SERVICE_VIEWS_PATH, default='views/')

        self.db_host = os.getenv(DB_HOST, None)
        self.db_port = int(os.getenv(DB_PORT, 3306))
        self.db_user = os.getenv(DB_USER, None)
        self.db_pass = os.getenv(DB_PASSWORD, None)
        self.db_name = os.getenv(DB_NAME, None)

        if None in (self.db_host, self.db_user, self.db_pass, self.db_name):
            raise Exception("Can't init service. Config not loaded")
