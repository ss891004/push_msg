from flask_restx import Resource
from main.ext import dbs
import requests
import json

class AccessToken(Resource):
    def get(self):
        print("1111111111111")
        token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww9985578839fbc0d9&corpsecret=y4HuwtCDJJOflzOPR-34hbuW7IWqFM02AhYMAwQEm9Y"
        r = requests.get(token_url) 
        return r.json()

    def post(self):
        print("accesstoken-post")
        pass
    def delete(self):
        print("accesstoken-delete")
        pass
    def put(self):
        print("accesstoken-put")
        pass

