from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
import platform
import uuid

# flask-sqlalchemy , flask-migrate
dbs = SQLAlchemy()
migrate = Migrate()

# initialize scheduler
scheduler = APScheduler()

from jobs.access_token import job_function
from datetime import datetime


def init_ext(app):
    dbs.init_app(app)
    migrate.init_app(app, dbs)

    scheduler.init_app(app)
    #立即执行
    scheduler.add_job(func=job_function, trigger='interval',seconds=10, next_run_time=datetime.now(), id=str(uuid.uuid1()))
    scheduler.start()
 