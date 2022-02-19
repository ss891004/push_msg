from main.ext import dbs
import time

class wx_token(dbs.Model):
    __tablename__ = 'wx_token'

    id = dbs.Column(dbs.Integer, primary_key=True,autoincrement=True)
    agent_id =  dbs.Column(dbs.String(10),nullable=False, default='')
    corp_id = dbs.Column(dbs.String(20),nullable=False, default='')
    corp_secret = dbs.Column(dbs.String(50),nullable=False, default='')
    access_token= dbs.Column(dbs.String(512),nullable=False, default='')
    err_code= dbs.Column(dbs.Integer)
    err_msg= dbs.Column(dbs.String(50), nullable=False, default='')
    expires_in=dbs.Column(dbs.Integer)
    insert_time = dbs.Column(dbs.String(20),nullable=False, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    def __init__(self):
        pass

    def __repr__(self):
        pass
