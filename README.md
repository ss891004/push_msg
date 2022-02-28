Flask CLI
    + https://www.jianshu.com/p/dcb4cecb2af7

python + mysql
    + 驱动 pymysql  
        + mysql+pymysql://username:password@server/db
    + mysqlclient
        + https://docs.sqlalchemy.org/en/14/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector


# Flask-Web
+ 一个项目，多个应用，多个API应用。
```
# 根据依赖文件列表，自动安装对应的软件包
pip install -r requirements.txt

# 使用pip导出依赖文件列表
pip freeze > requirements.txt	

列出可升级的包：pip list --outdate
升级一个包：pip install --upgrade

python3自带的虚拟环境：python -m venv venv 

```

### python-dotenv



### flask-migrate

+ set/export FLASK_APP=server.py

```
flask db init      初始化迁移环境 生成 migrations文件夹 （首次执行会生成migrations文件夹）
flask db migrate   生成 versions 下的迁移文件
flask db upgrade   将表映射到数据库中去

如果改变了模型，只需要执行命令 2 和 3 即可。

```
+ No changes in schema detected.
    + 虽然model 已经创建，但是在迁移时，需要让项目知道此model的存在。

+ alembic_version
    + 项目在迁移时候，一定要注意版本的一致


### flask-blueprint



### flask-restx

#### REST
+ REST即Representational State Transfer的缩写。REST最大的几个特点为：资源、统一接口、URI和无状态。
 + 资源：网络上的一个实体或具体信息。JSON是现在最常用的资源表示格式。
 + 统一接口：数据的元操作，即CRUD操作，分别对应于HTTP方法：
    + GET用来获取资源
    + POST用来新建资源（也可用于更新资源）
    + PUT用来更新资源
    + DELETE用来删除资源。
 + URI：URI是每一个资源的地址或识别符。最典型的URI即URL。
 + 无状态：所有的资源，都可以通过URI定位，而且这个定位与其他资源无关，也不会因为其他资源的变化而改变。


+ 命名空间 (Namespace)
    + 作用是为不同的资源，不同的url分组


#### werkzeug.datastructures.FileStorage


#### Coloum
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

```

新建一个 schedulers (调度器) 。
添加一个调度任务(job stores)。
运行调度任务

APScheduler 有四种组件，分别是：调度器(scheduler)，作业存储(job store)，触发器(trigger)，执行器(executor)。
```

+ RuntimeError: No application found . Either work inside a view function or push an application context
```
报错原因：线程是独立的，相对于flask进程是独立的，它不知道flask初始化时候，app对象，db对象是谁，也就拿不到连接数据库需要的config，就报错了。
```

```
flask 中如下两个字段

create_time1 = db.Column(db.DateTime, default=datetime.now)
create_time2 = db.Column(db.DateTime, default=datetime.now())

两者的区别:
第一个插入的是期望的, 数据的插入时间，每条数据插入时可自动根据当前时间生成

第二条是一个固定的时间, 程序部署的时间，所有的数据都是这个固定时间

实际上默认值在mysql数据库没有体现, 都是sqlalchemy在插入数据时加的

如果想想在生成的table中有默认值使用server_default

name = db.Column(db.String(45), server_default='hh')
当我们要给布尔值类型指定server_default时，需要用到text

from sqlalchemy import text
is_domain = db.Column(db.Boolean,default=False,server_default=text('0'))
 

因为mysql的datetime类型的数据不支持函数, 所以没法指定默认值位当前时间

记录每次修改的时间,onupdate
update_time = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)
```


## python 解析JSON数据


|Python对象|JSON|
|---|---|
|dict|object|
|list, tuple|array|
|str|string|
|int, float|number|
|True|true|
|False|false|
|None|null|

+ Python 对象编码成 JSON，dump()和dumps()
+ JSON 数据转换成 Python 对象，使用load()和loads()

## 类
+ 类的方法的定义
    def fun_name(self,...);
      Pass

    其中的参数self代表类的实例，在调用方法时由系统自动提供
    方法定义时必须指明self参数

 
+ 类的方法的调用
    1.类的内部调用：self.<方法名>(参数列表)。
    2.在类的外部调用：<实例名>.<方法名>(参数列表)。
    注意：以上两种调用方法中，提供的参数列表中都不用包括self。


## 问题点
+ Object of type Response is not JSON serializable
    + 返回的对象必须可系列化
+ the JSON object must be str, bytes or bytearray, not Response


## flask-sqlalchemy

|属性|说明|
|---|---|
|SQLALCHEMY_DATABASE_URI|用于连接数据的数据库。例如： sqlite:tmp/test.db mysql://username:password@server/db|
|SQLALCHEMY_BINDS|一个映射绑定 (bind) 键到 SQLAlchemy 连接 URIs 的字典。 更多的信息请参阅 绑定多个数据库。|
|SQLALCHEMY_ECHO|如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助。|
|SQLALCHEMY_RECORD_QUERIES|可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用。更多信息请参阅 get_debug_queries()。|
|SQLALCHEMY_NATIVE_UNICODE|可以用于显式地禁用支持原生的 unicode。这是 某些数据库适配器必须的（像在 Ubuntu 某些版本上的 PostgreSQL），当使用不合适的指定无编码的数据库 默认值时。|
|SQLALCHEMY_POOL_SIZE|数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。|
|SQLALCHEMY_POOL_TIMEOUT|指定数据库连接池的超时时间。默认是 10。|
|SQLALCHEMY_POOL_RECYCLE|自动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。|
|SQLALCHEMY_MAX_OVERFLOW|控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。|
|SQLALCHEMY_TRACK_MODIFICATIONS|如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。|

+ 增
    + db.session.add()
    + db.session.add_all()
    + db.session.commit()

+ 删
    + db.session.delete()

+ 改
    + 修改对象中的属性
    + db.session.commit()

+ 查
    + Student.query.all()
    + student = Student.query.filter_by(age = 18) #按条件查询
    + student = Student.query.get(1) #自动以主键查询
    + student = Student.query.group_by("age") #按照组
    + student = Student.query.order_by(Student.age) #排序
    + student = Student.query.order_by(Student.age.desc()) #按照组


+ 表关系：
    + 一对一
    + 一对多
    + 多对多

***
---
___
## 部署情况

+ 环境遍历获取
    + .bashrc
        + FLASK_ENV=

+ 数据第一次迁移
    flask db init
    flask db migrate
    flask db upgrade

+ Target database is not up to date.

+ 多进程部署，定时任务多次执行
    +  apscheduler.schedulers.SchedulerAlreadyRunningError: Scheduler is already running