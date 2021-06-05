from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from pathseeker.src.config.flask_app_config import FLASK_DEBUG, FLASK_HOST, FLASK_PORT
from pathseeker.src.flask_app.app import PathSeekerApp

PATHSEEKER_APP = PathSeekerApp(host=FLASK_HOST, debug=FLASK_DEBUG, port=FLASK_PORT)
APP: Flask = PATHSEEKER_APP.app
DATABASE: SQLAlchemy = PATHSEEKER_APP.database
