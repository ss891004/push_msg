
# http://127.0.0.1:8080/TextMessage?hrcbTemplateIds=&hrcbContent=null&agentId=1000012&hrcbToUser=06400730|587

from flask_restx import Resource,reqparse
from main.setting import token_sources, send_message_post_url
import json
from models.wx_user import WxUser
import requests
from jobs.access_token import token_job
from utils.qywx import get_qywx_user_id

class TextMsg2(Resource):

    def send(self, msg_data):

        msg_data['hrcb_user'] = get_qywx_user_id(msg_data['hrcb_user'])

        msg_json={
   "touser" : msg_data['hrcb_user'],
   "msgtype" : "text",
   "agentid" : msg_data['agent_id'],
   "text" : {
       "content" : msg_data['content']
   },
   "safe":0,
   "enable_id_trans": 0,
   "enable_duplicate_check": 0,
   "duplicate_check_interval": 1800}

        # 异常处理
        msg_url =send_message_post_url % (token_sources[str(msg_data['agent_id'])])
        r= requests.post(msg_url, json=msg_json)

        # 响应JSON
        '''
        {
        "errcode": 0,
        "errmsg": "ok",
        "msgid": "fcLc6UhB2absSaoEDgOVFEw3tNJHReZX9_WLAKmrP4UVtPE1CHKz6c5Z54XPVzwpO0QEbp523VmEc5czDU6Lcg"
        }
        '''
        r_dict = json.loads(r.text)
        if r_dict["errcode"] == 0 :
            return {'msg':'OK','data': r_dict['msgid']} ,201
        elif r_dict["errcode"] == 40014 :  # invalid access_token
            # 重新获取access_token
            token_job(msg_data['agent_id'])
            msg_url =send_message_post_url % (token_sources[str(msg_data['agent_id'])])
            r= requests.post(msg_url, json=msg_json)
            return {'msg':'OK','data': r_dict} ,201
        else:
            return {'msg':'Failed','data': r_dict} ,409

    def get(self):

        parse = reqparse.RequestParser()
        parse.add_argument('hrcbTemplateIds', type=str)
        parse.add_argument('hrcbContent', type=str,required=True)
        parse.add_argument('agentId', type=str,required=True)
        parse.add_argument('hrcbToUser', type=str,required=True)

        args = parse.parse_args()
        if not args:
            abort(400, "need request data")
        else:
            data={}
            data['hrcb_user']=args.get('hrcbToUser')
            data['agent_id']=args.get('agentId')
            data['content']=args.get('hrcbContent')
            return self.send(data)
            

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('hrcbTemplateIds', type=str)
        parse.add_argument('hrcbContent', type=str ,required=True)
        parse.add_argument('agentId', type=str ,required=True)
        parse.add_argument('hrcbToUser', type=str ,required=True)

        args = parse.parse_args()
        if not args:
            abort(400, "need request data")
        else:
            data={}
            data['hrcb_user']=args.get('hrcbToUser')
            data['agent_id']=args.get('agentId')
            data['content']=args.get('hrcbContent')
            return self.send(data)