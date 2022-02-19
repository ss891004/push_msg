from main.ext import dbs
import time

class WxMessage(dbs.Model):
    __tablename__ = 'wx_message'

    id = dbs.Column(dbs.Integer, primary_key=True,autoincrement=True)
    from_ip = dbs.Column(dbs.String(40))
    from_system = dbs.Column(dbs.String(40))
    txn_time =  dbs.Column(dbs.String(14))
    to_user =  dbs.Column(dbs.Text)
    user_id =  dbs.Column(dbs.String(50))
    to_party =  dbs.Column(dbs.Text)
    to_tag =  dbs.Column(dbs.Text)
    msg_type  =  dbs.Column(dbs.String(50))
    agent_id   =  dbs.Column(dbs.String(10))
    msg_content =   dbs.Column(dbs.Text)
    media_id  =   dbs.Column(dbs.Text)
    msg_title  =   dbs.Column(dbs.String(50))
    msg_desc =   dbs.Column(dbs.String(100))
    msg_url= dbs.Column(dbs.Text)
    insert_time = dbs.Column(dbs.String(20),nullable=False, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


    def __init__(self):
        pass

    def __repr__(self):
        pass
        
