from flask import Flask

from .ext import init_ext

from .setting import envs

from apis import init_api

def create_app():
    app = Flask(__name__)

    # 加载settings中的配置
    app.config.from_object(envs.get('develop'))

    print(app.config)

    # 加载扩展库
    init_ext(app)

    # 加载路由

    init_api(app)


    return app