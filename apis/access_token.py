from flask_restx import Namespace,Resource,fields,reqparse
from main.ext import dbs
from models import wx_token
import requests
import json




class AccessToken(Resource):
        
    def get(self):
        token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww9985578839fbc0d9&corpsecret=y4HuwtCDJJOflzOPR-34hbuW7IWqFM02AhYMAwQEm9Y"
        r = requests.get(token_url) 
        return r.json()

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('agentid', type=str, required=True, help='app agent id')
        parser.add_argument('corpsecret', type=str, required=True, help='app corp secret')

        args = parser.parse_args()
        print(args)
        print(type(args))
        print(args.get("agentid"))
        print(args.get("corpsecret"))
        #app_token = wx_token.query.filter_by(agent_id= args["agentid"]).first()
        if True:
            app_token=wx_token(agent_id=args.get("agentid"),corp_secret= args.get("corpsecret"))
            dbs.session.add(app_token)
            dbs.session.commit()
        print("accesstoken-post")
        pass

