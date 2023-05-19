from datetime import timedelta

SECRET_KEY = 'Ak+NMzarpmGp8rpwQaeJtUM5TER7x6pyfSiDtJ8nzh5t1G+0tJryBa4d'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@winhost/supersetdb3'
# SECRET_KEY = '\2\1thisismyscretkey\1\2\\e\\y\\y\\h'
APP_NAME = "EFFIOS_SUPERSET"
APP_ICON = "/static/assets/images/Ministry_logo.png"
LOGO_TARGET_PATH = '/'
FAVICONS = [{"href": "/static/assets/images/Ministry_logo.ico"}]

LANGUAGES = {'en': {'flag': 'us', 'name': 'English'},
             'fr': {'flag': 'fr', 'name': 'Français'}}
BABEL_DEFAULT_LOCALE = "fr"

SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=2).total_seconds())

FAB_INDEX_VIEW = "superset.custom.welcome.custom_index.SupersetDashboardIndexView"
