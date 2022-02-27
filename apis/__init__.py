
from flask_restx import Api
from flask import Blueprint

from .media import media
from .message import msg
from .message.send_file_msg import FileMsg
from .message.send_text_msg import TextMsg
from .media.upload_media import UploadMedia
from .text_msg import TextMsg2

api =Api()

def init_api(app):
    api.init_app(app, version='1.0', title='企业微信消息推送 API',description='企业微信消息推送 API',)

# 注册资源，使用单独的命名空间
# api.add_namespace(ns1,path='/api/v1')
api.add_namespace(media)
api.add_namespace(msg)
api.add_resource(TextMsg2,'/TextMessage')
