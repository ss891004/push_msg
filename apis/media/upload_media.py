from flask_restx import Namespace,fields,Resource,reqparse
from werkzeug.datastructures import FileStorage
from models import wx_message,wx_token,wx_user
from main.setting import token_sources,upload_media_path,upload_media_post_url
import requests
import json
from . import media as ns
import os
from datetime import datetime
import fnmatch

'''
媒体文件类型，分别有图片（image）、语音（voice）、视频（video），普通文件（file）
上传的媒体文件限制:
图片（image）：10MB，支持JPG,PNG格式
语音（voice） ：2MB，播放长度不超过60s，仅支持AMR格式
视频（video） ：10MB，支持MP4格式
普通文件（file）：20MB
'''

parser = reqparse.RequestParser()
parser.add_argument('imgFile', type=FileStorage,required=True, location='files') 
parser.add_argument('agent_id', type=int, required=True)


@ns.route('/upload')
class UploadMedia(Resource):

    @ns.expect(parser)
    def post(self):
        # 获取客户端上传的文件
        args = parser.parse_args()
        img_file = args['imgFile']  # FileStorage instance
        file_path= os.path.join(upload_media_path, datetime.now().strftime('%Y-%m'))
        # 创建目录
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        full_file_path= os.path.join(file_path,img_file.filename)

        # 文件大小


        # 重名处理
        if os.path.exists(full_file_path):
            dot_index = img_file.filename.rindex('.')
            prefix_file_name = img_file.filename[0:dot_index] 

            file_count = len(fnmatch.filter(os.listdir(file_path), prefix_file_name +'*'))

            if file_count==0:
                file_count=1
                
            new_file_name =img_file.filename[0:dot_index]+'_'+str(file_count)+'.'+ img_file.filename[dot_index+1:]
        else:
            new_file_name= img_file.filename
        
        full_file_path = os.path.join(file_path,new_file_name)
        # 保存文件
        img_file.save(full_file_path)
        
        agent_id =str(args.get('agent_id'))

        if agent_id in token_sources :
            # 将本地文件上传给微信服务器
            file_url= upload_media_post_url % ( token_sources[agent_id], 'file')
            files = {'media': open(full_file_path, 'rb')}  # filename、filelength、content-type
            r= requests.post(file_url,files=files)

            return {'msg':'OK', 'data':(json.loads(r.text))['media_id']} ,201

        else :
            return {'msg':'agent_id not exists.'}, 409
