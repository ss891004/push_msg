from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

dbs = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    dbs.init_app(app)
    migrate.init_app(app, dbs)