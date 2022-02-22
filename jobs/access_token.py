import requests
import json
from models.wx_token import WxToken
from main.ext import scheduler
import uuid
from datetime import datetime

def job_function():
    print( datetime.now())
    # token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww9985578839fbc0d9&corpsecret=y4HuwtCDJJOflzOPR-34hbuW7IWqFM02AhYMAwQEm9Y"
    # r = requests.get(token_url) 
    # return r.json()
    token = WxToken()
    token.access_token =str(uuid.uuid1())
    # 在任务中获取程序上文进行操作
    with scheduler.app.app_context():

        # 更新所有应用的access token
        token_list =   WxToken.query.all()
        for s in token_list:
            print(s.id)
            print(s.agent_id)
            print(s.corp_id)
            print(s.corp_secret)

        #token.save()
