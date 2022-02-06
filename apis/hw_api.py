import imp
from random import random
from flask_restx import Resource
from models.user import User
from main.ext import dbs
import random
import json

class HelloWorld(Resource):
    def get(self):

        user1 = User(UserCode="yyyy", Password="xxxxxxx")
        dbs.session.add(user1)
        dbs.session.commit()
        return {'hello': json.dumps(user1)}

    def post(self):
        return {'hello': 'world'}