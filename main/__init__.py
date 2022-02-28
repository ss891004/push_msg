from flask import Flask

from .ext import init_ext

from .setting import envs

from apis import init_api

import os

def create_app():
    app = Flask(__name__)

    # 加载settings中的配置

    env = os.environ.get('FLASK_ENV')
    if env not in envs:
        env ='development'
    print(env)
    app.config.from_object(envs.get(env))

    print(app.config)

    # 加载扩展库
    init_ext(app)

    # 加载rest api
    init_api(app)

    return app