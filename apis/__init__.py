
from flask_restx import Api

from .upload_media import ns as upload_media_ns

api =Api()

def init_api(app):
    api.init_app(app, version='1.0', title='企业微信消息推送 API',description='企业微信消息推送 API',)

# 注册资源，使用单独的命名空间
api.add_namespace(upload_media_ns)
