import os

import flask
import flask_sqlalchemy


class PathSeekerApp:
    def __init__(
        self,
        host: str = "0.0.0.0",
        debug: bool = False,
        port: int = int(os.environ.get("PORT", 8080)),
    ):
        self._app = flask.Flask(__name__)
        self._debug = debug
        self._host = host
        self._port = port

        self._app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ePXImvuAak3DqWOmJpqb@localhost/pathseeker'

        self._db = flask_sqlalchemy.SQLAlchemy(self._app)

    def get_app(self) -> flask.Flask:
        return self._app

    def get_db(self) -> flask_sqlalchemy.SQLAlchemy:
        return self._db

    def run(self) -> None:
        self._app.run(host=self._host, debug=self._debug, port=self._port)


PATHSEEKER_APP = PathSeekerApp(host="localhost", debug=True, port=5000)
APP = PATHSEEKER_APP.get_app()
DB = PATHSEEKER_APP.get_db()


class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(80), unique=True, nullable=False)
    email = DB.Column(DB.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    DB.create_all()
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    DB.session.add(admin)
    DB.session.add(guest)
    DB.session.commit()

    print(User.query.all())
    print(User.query.filter_by(username='admin').first())
