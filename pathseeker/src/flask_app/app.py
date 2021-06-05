from os import environ
from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from pathseeker.src.config.mysql_config import MYSQL_CONNECTION_STRING
from pathseeker.src.logging.logging_manager import LoggingManager

LOGGER = LoggingManager.get_logger(Path(__file__).name)


class PathSeekerApp:
    def __init__(
        self,
        host: str = "0.0.0.0",
        debug: bool = False,
        port: int = int(environ.get("PORT", 8080)),
        database_url: str = MYSQL_CONNECTION_STRING,
        database_track_modifications: bool = False,
    ):
        self.__app = Flask(__name__)
        self.__debug = debug
        self.__host = host
        self.__port = port

        self.__app.config["SQLALCHEMY_DATABASE_URI"] = database_url
        self.__app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = database_track_modifications

        self.__db = SQLAlchemy(self.__app)

    @property
    def app(self) -> Flask:
        return self.__app

    @property
    def database(self) -> SQLAlchemy:
        return self.__db

    def run(self) -> None:  # pragma: no cover
        # TODO test server run when server has endpoints
        LOGGER.info(
            "Starting app with host %s port %s %s", self.__host, self.__port, "in debug" if self.__debug else ""
        )
        self.__app.run(host=self.__host, debug=self.__debug, port=self.__port)
