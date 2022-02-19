Flask CLI
    + https://www.jianshu.com/p/dcb4cecb2af7

python + mysql
    + 驱动 pymysql  
        + mysql+pymysql://username:password@server/db
    + mysqlclient
    + https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector


# Flask-Web
Flask web project

一个项目，多个应用，多个API应用。
```
# 使用pip导出依赖文件列表
pip install -r requirements.txt

pip freeze > requirements.txt	

# 根据依赖文件列表，自动安装对应的软件包
pip install -r requirements.txt


列出可升级的包：pip list --outdate
升级一个包：pip install --upgrade

```
### python-dotenv

+ flask-migrate

## flask-migrate
```
init migrate upgrade
模型 --> 迁移文件 --> 表

set/export FLASK_APP=server.py

flask db init     初始化迁移环境 生成 migrations文件夹 （首次执行会生成migrations文件夹）
flask db migrate   生成 versions 下的迁移文件
flask db upgrade   将表映射到数据库中去
如果改变了模型，只需要执行命令 2 和 3 即可。

+ No changes in schema detected.
    + 虽然model 已经创建，但是在迁移时，需要让项目知道此model的存在。

+ alembic_version
    + 项目在迁移时候，一定要注意版本的一致

```

### flask-blueprint



### Coloum
+ Id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False, unique=True, index=True)

### alembic 

### SQLAlchemy


### 序列化和反序列化


### flask-apscheduler
+ https://github.com/viniciuschiele/flask-apscheduler/tree/master/examples

```
Configuration
Configuration options specific to Flask-APScheduler:

SCHEDULER_API_ENABLED: bool (default: False)
SCHEDULER_API_PREFIX: str (default: "/scheduler")
SCHEDULER_ENDPOINT_PREFIX: str (default: "scheduler.")
SCHEDULER_ALLOWED_HOSTS: list (default: ["*"])
Configuration options specific to APScheduler:

SCHEDULER_JOBSTORES: dict
SCHEDULER_EXECUTORS: dict
SCHEDULER_JOB_DEFAULTS: dict
SCHEDULER_TIMEZONE: dict
```



## 问题点
+ Object of type Response is not JSON serializable
    + 返回的对象必须可系列化
+ the JSON object must be str, bytes or bytearray, not Response