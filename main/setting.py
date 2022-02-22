import os
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    ENV='development'
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "flask"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    SCHEDULER_API_ENABLED = True
    #SCHEDULER_JOBSTORES={'default':SQLAlchemyJobStore(url=get_db_uri(dbinfo))}
    #SCHEDULER_EXECUTORS={'default': {'type': 'threadpool', 'max_workers': 10} }


class ProductConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "mysqldb",
        "USER": "root",
        "PASSWORD": " ",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": " "
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

envs = {
    "develop": DevelopConfig,
    "product": ProductConfig
}

corpid="ww9985578839fbc0d9"
access_token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET"

token_sources = {}

class TokenConfig:
    token_sources['1000012'] = {
        'corpsecret': 'FP9vhJs3sWgt8jUKwwPL2zYoEyBMRv5SNtBppIYSiGw',
        'access_token':''
    }
    

   
   
