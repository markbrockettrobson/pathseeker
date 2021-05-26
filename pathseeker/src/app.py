from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class PathSeekerApp:
    def __init__(self, host: str = "0.0.0.0", debug: bool = False, port: int = int(environ.get("PORT", 8080))):
        self.__app = Flask(__name__)
        self.__debug = debug
        self.__host = host
        self.__port = port

        self.__app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:ePXImvuAak3DqWOmJpqb@localhost/pathseeker"
        self.__app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        self.__db = SQLAlchemy(self.__app)

    @property
    def app(self) -> Flask:
        return self.__app

    @property
    def database(self) -> SQLAlchemy:
        return self.__db

    def run(self) -> None:  # pragma: no cover
        # TODO test server run when server has endpoints
        self.__app.run(host=self.__host, debug=self.__debug, port=self.__port)


PATHSEEKER_APP = PathSeekerApp(host="localhost", debug=True, port=5000)
APP = PATHSEEKER_APP.app
DATABASE = PATHSEEKER_APP.database


def main():  # pragma: no cover
    DATABASE.create_all()


if __name__ == "__main__":  # pragma: no cover
    main()
