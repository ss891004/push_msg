
from flask_restx import Api
from .hw_api import HelloWorld
from .todo_api import ns

api =Api()

def init_api(app):
    api.init_app(app, version='1.0', title='TodoMVC API',description='A simple TodoMVC API',)

# 注册资源
api.add_resource(HelloWorld, '/world')

api.add_namespace(ns,path='/bbbbb')
