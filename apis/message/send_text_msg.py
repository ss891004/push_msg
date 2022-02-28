from flask_restx import Namespace,fields,Resource,reqparse
from werkzeug.datastructures import FileStorage
from main.setting import token_sources, send_message_post_url
from models.wx_user import WxUser
import requests
import json
from . import msg as ns
from utils.qywx import get_qywx_user_id

# 请求参数的json格式
TextData=ns.model('TextData',
{
'hrcb_user':fields.String(required=True,description='员工工号,多个工号用|连接'),
'hrcb_party':fields.String(description='可省略'),
'agent_id':fields.Integer(description='应用id'),
'content':fields.String(required=True,description='发送的内容'),
})

# get请求的参数
parser = reqparse.RequestParser()
parser.add_argument('hrcb_user', type=str,required=True,help='员工工号,多个工号用|连接')
parser.add_argument('hrcb_party', type=str,help='可省略')
parser.add_argument('agent_id', type=int,required=True,help='应用id' )
parser.add_argument('content', type=str,required=True,help='发送的内容')


@ns.route('/text')
class TextMsg(Resource):

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
   "duplicate_check_interval": 1800
}

        # 异常处理
        agent_secret = str(msg_data['agent_id'])
        if agent_secret in token_sources:
            msg_url =send_message_post_url % (token_sources[agent_secret])
            r= requests.post(msg_url, json=msg_json)

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

    @ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        print(args)
        return self.send(args)

    @ns.expect(TextData)
    def post(self):
        print(ns.payload)
        return self.send(ns.payload)