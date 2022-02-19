from flask_restx import Namespace,fields,Resource
from models import wx_message,wx_token,wx_user

ns = Namespace('upload', description='上传临时素材')


@ns.route('/media')
class UploadMedia(Resource):
    def get(self, **kwargs):
        print(kwargs)
        pass
    def post(self):
        pass
    def delete(self):
        pass
    def put(selt):
        pass