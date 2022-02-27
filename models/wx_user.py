from main.ext import dbs
from datetime import datetime

class WxUser(dbs.Model):
    __tablename__ = 'wx_user'

    emp_no = dbs.Column(dbs.String(10), primary_key=True)
    wx_user_id = dbs.Column(dbs.String(50), unique=True, index=True)
    emp_name = dbs.Column(dbs.String(50))
    emp_phone= dbs.Column(dbs.String(50))
    emp_cert_id = dbs.Column(dbs.String(20))
    emp_position = dbs.Column(dbs.String(100))
    emp_depart = dbs.Column(dbs.String(50))
    create_time = dbs.Column(dbs.DateTime, default=datetime.now)
    update_time = dbs.Column(dbs.DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def save(self):
        dbs.session.add(self)
        dbs.session.commit()