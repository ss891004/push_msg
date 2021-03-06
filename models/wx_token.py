from main.ext import dbs
from datetime import datetime

class WxToken(dbs.Model):
    __tablename__ = 'wx_token'

    id = dbs.Column(dbs.Integer, primary_key=True, autoincrement=True)
    agent_id =  dbs.Column(dbs.String(10),nullable=False, default='')
    corp_id = dbs.Column(dbs.String(20),nullable=False, default='')
    corp_secret = dbs.Column(dbs.String(50),nullable=False, default='')
    access_token= dbs.Column(dbs.String(512),nullable=True, default='')
    err_code= dbs.Column(dbs.Integer)
    err_msg= dbs.Column(dbs.String(50), nullable=True, default='')
    expires_in=dbs.Column(dbs.Integer)
    create_time = dbs.Column(dbs.DateTime, default=datetime.now)
    update_time = dbs.Column(dbs.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()

    def update(self):
        dbs.session.commit()