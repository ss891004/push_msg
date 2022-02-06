pip freeze > requirements.txt	
# 使用pip导出依赖文件列表

pip install -r requirements.txt
# 根据依赖文件列表，自动安装对应的软件包

pip install python-dotenv

Flask CLI
    + https://www.jianshu.com/p/dcb4cecb2af7


python + mysql
    + 驱动 pymysql  
        + mysql+pymysql://username:password@server/db
    + mysqlclient
    + https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector


init migrate upgrade
模型 --> 迁移文件 --> 表

python manage.py db init 初始化迁移环境 生成 migrations文件夹 （首次执行会生成migrations文件夹）
python manage.py db migrate 生成 versions 下的迁移文件
python manage.py db upgrade 将表映射到数据库中去
如果改变了模型，只需要执行命令 2 和 3 即可。

+ No changes in schema detected.
    + 虽然model 已经创建，但是在迁移时，需要让项目知道此model的存在。

+ alembic_version
    + 项目在迁移时候，一定要注意版本的一致


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