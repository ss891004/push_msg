from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

# flask-sqlalchemy , flask-migrate
dbs = SQLAlchemy()
migrate = Migrate()

# initialize scheduler
scheduler = APScheduler()

def job_function():
    print("aaa")


def init_ext(app):
    dbs.init_app(app)
    migrate.init_app(app, dbs)

    scheduler.init_app(app)

    #scheduler.add_job(func=job_function, trigger='interval',seconds=2, id='my_job_id')

    scheduler.start()