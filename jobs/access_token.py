import requests
import json
from models.wx_token import WxToken
from main.ext import scheduler
import uuid
from datetime import datetime
from main.setting import token_sources

def token_job(agent_id=None):
    print( datetime.now())
    # 在任务中获取程序上文进行操作
    with scheduler.app.app_context():
        # 更新所有应用的access token
        try:
            if agent_id is None:
                token_list = WxToken.query.all()
            else:
                token_list = WxToken.query.filter_by(agent_id=agent_id)
        except: 
            return 

        for s in token_list:
            token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (s.corp_id,s.corp_secret)
            r = requests.get(token_url) 
            b = json.loads(r.text)

            s.access_token= b.get("access_token")
            s.update()
            token_sources[s.agent_id]=s.access_token

        print(token_sources)
