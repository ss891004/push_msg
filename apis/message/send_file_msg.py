from flask_restx import Namespace,fields,Resource,reqparse
from werkzeug.datastructures import FileStorage
from models.wx_user import WxUser
from main.setting import token_sources, send_message_post_url
import requests
import json
from . import msg as ns
from utils.qywx import get_qywx_user_id


# 请求参数的json格式
FileData=ns.model('FileData',
{
'hrcb_user':fields.String(required=True),
'agent_id':fields.Integer,
'media_id':fields.String(required=True),
})

# get请求的参数
parser = reqparse.RequestParser()
parser.add_argument('hrcb_user', type=str, required=True)
parser.add_argument('agent_id', type=int, required=True)
parser.add_argument('media_id', type=str, required=True)


@ns.route('/file')
class FileMsg(Resource):

    def send(self,msg_data):

        msg_data['hrcb_user'] = get_qywx_user_id(msg_data['hrcb_user'])

        msg_json ={
            "touser" : msg_data['hrcb_user'] ,
            "msgtype" :'file',
            "agentid" :msg_data['agent_id'],
            "file" : {
                "media_id" :  msg_data['media_id']
                },
            "safe":0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }

        # 异常处理
        agent_secret = str(msg_data['agent_id'])
        if agent_secret in token_sources:
            file_message_url =send_message_post_url % (token_sources[agent_secret])
            r= requests.post(file_message_url, json=msg_json)

            r_dict=json.loads(r.text)

            if r_dict["errcode"] == 0 :
                return {'msg':'OK','data': r_dict['msgid']} ,201
            elif r_dict["errcode"] == 40014 :  # invalid access_token
                # 重新获取access_token
                token_job(msg_data['agent_id'])
                msg_url =send_message_post_url % (token_sources[str(msg_data['agent_id'])])
                r= requests.post(msg_url, json=msg_json)
                return {'msg':'OK','data': r_dict} ,201
        else:
            return {'msg':'Failed','data': 'this agent_id not exists.'} ,409
        # 响应JSON
        '''
{
  "errcode": 0,
  "errmsg": "ok",
  "msgid": "fcLc6UhB2absSaoEDgOVFIk9BaynI6JIcT95PMi3J9TBGcWrhMqsbVsahG0-b8eOUxkTMKZbXenVfckB1TtJHQ"
}
        '''

    @ns.expect(parser)
    def get(self):
        args = parser.parse_args()
        print(args)
        return self.send(args)

    @ns.expect(FileData)
    def post(self):
        print(ns.payload)
        return self.send(ns.payload)