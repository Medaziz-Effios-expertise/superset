from datetime import timedelta
from superset.superset_typing import CacheConfig
from cachelib.redis import RedisCache
from celery.schedules import crontab
"""
from flask_appbuilder.security.manager import AUTH_OID
from superset.Keycloak.security_manager import OIDCSecurityManager
"""
SECRET_KEY = '\2\1thisismyscretkey\1\2\\e\\y\\y\\h'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@winhost/supersetdb'

APP_NAME = "EFFIOS_SUPERSET"
APP_ICON = "/static/assets/images/Ministry_logo.png"
LOGO_TARGET_PATH = '/'
FAVICONS = [{"href": "/static/assets/images/Ministry_logo.ico"}]
"""
AUTH_TYPE = AUTH_OID
OIDC_CLIENT_SECRETS = r'/home/ubuntu/superset/superset/Keycloak/keycloak_settings.json'
OIDC_ID_TOKEN_COOKIE_SECURE = False
OIDC_REQUIRE_VERIFIED_EMAIL = False
CUSTOM_SECURITY_MANAGER = OIDCSecurityManager
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
"""
LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    'fr': {'flag': 'fr', 'name': 'Français'}
}
BABEL_DEFAULT_LOCALE = "fr"

FEATURE_FLAGS = {
    "ROW_LEVEL_SECURITY": True,
    "ALERT_REPORTS": True,
    "DASHBOARD_RBAC": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "GLOBAL_ASYNC_QUERIES": True
}

SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=2).total_seconds())

# Metadata cache
CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:redis@127.0.0.1:6379/1'
}

# Charting data queried from datasets cache
DATA_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_data_',
    'CACHE_REDIS_URL': 'redis://redis:redis@127.0.0.1:6379/2'
}

# Dashboard filter state cache
FILTER_STATE_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_filter_cache',
    'CACHE_REDIS_URL': 'redis://redis:redis@127.0.0.1:6379/3'
}

# Charting data queried from datasets
EXPLORE_FORM_DATA_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_explore_',
    'CACHE_REDIS_URL': 'redis://redis:redis@127.0.0.1:6379/4'
}


# Async queries config
# To enable, in FEATURE_FLAGS add this "GLOBAL_ASYNC_QUERIES": True
GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
    "port": 6379,
    "host": "127.0.0.1",
    "username": "redis",
    "password": "redis",
    "db": 0,
    "ssl": False,
}

GLOBAL_ASYNC_QUERIES_JWT_SECRET = "db603cd6463e426fa7134547ca281e4b976a777f2f6211c4ac3a1928f7c2b702"


class CeleryConfig(object):
    broker_url = 'redis://redis:redis@127.0.0.1:6379/0'
    imports = (
        'superset.sql_lab',
        'superset.tasks',
        'superset.tasks.thumbnails',
    )
    result_backend = 'redis://redis:redis@127.0.0.1:6379/0'
    worker_log_level = 'DEBUG'
    worker_prefetch_multiplier = 10
    task_acks_late = True
    task_annotations = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 600,
            'soft_time_limit': 600,
            'ignore_result': True,
        },
    }
    beat_schedule = {
        'cache-warmup-hourly': {
            'task': 'cache-warmup',
            'schedule': crontab(minute=1, hour='*'),  # @hourly
            'kwargs': {
                    'strategy_name': 'top_n_dashboards',
                    'top_n': 10,
                    'since': '7 days ago',
            },
        },
        'email_reports.schedule_hourly': {
            "task": "email_reports.schedule_hourly",
            "schedule": crontab(minute=1, hour="*"),
        },
        'reports.scheduler': {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        'reports.prune_log': {
            "task": "reports.prune_log",
            "schedule": crontab(minute=0, hour=0),
        },
    }


RESULTS_BACKEND = RedisCache(host='127.0.0.1', port=6379,
                             key_prefix='superset_results', username='redis', password='redis')

CELERY_CONFIG = CeleryConfig

# Email configuration
SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
SMTP_STARTTLS = True
SMTP_SSL_SERVER_AUTH = False
SMTP_SSL = False
SMTP_USER = "10935acefed033"
SMTP_PASSWORD = "d2b59467dc5382"
SMTP_MAIL_FROM = "superset@effios.fr"
EMAIL_REPORTS_SUBJECT_PREFIX = "[Superset-EFFIOS] "
# WebDriver configuration
# If you use Firefox, you can stick with default values
# If you use Chrome, then add the following WEBDRIVER_TYPE and WEBDRIVER_OPTION_ARGS

WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
    "--headless",
    "--marionette",
]

SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600
"""
WEBDRIVER_OPTION_ARGS = ["--headless", "--marionette"]
"""
# This is for internal use, you can keep http
WEBDRIVER_BASEURL = "http://localhost:8088"
# This is the link sent to the recipient. Change to your domain, e.g. https://superset.mydomain.com
WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL
THUMBNAIL_SELENIUM_USER = 'admin'
ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
