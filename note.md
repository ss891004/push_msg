# Flask-Web
Flask web project

一个项目，多个应用，多个API应用。
```
pip install -r requirements.txt

pip freeze > requirements.txt	

python main.py

```

## 使用的插件
+ flask-blueprint


+ pip install Flask-APScheduler
    + https://github.com/viniciuschiele/flask-apscheduler
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