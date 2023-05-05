from datetime import timedelta

#from flask_appbuilder.security.manager import AUTH_OID
#from superset.Keycloak.security_manager import OIDCSecurityManager
from superset.views.custom_views import LegalView, RGPDView

SECRET_KEY = 'Ak+NMzarpmGp8rpwQaeJtUM5TER7x6pyfSiDtJ8nzh5t1G+0tJryBa4d'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@winhost/supersetdb2'
# SECRET_KEY = '\2\1thisismyscretkey\1\2\\e\\y\\y\\h'
APP_NAME = "EFFIOS_SUPERSET"
APP_ICON = "/static/assets/images/Ministry_logo.png"
LOGO_TARGET_PATH = '/'
FAVICONS = [{"href": "/static/assets/images/Ministry_logo.ico"}]
""""
AUTH_TYPE = AUTH_OID
OIDC_CLIENT_SECRETS = r'/home/main_superset/superset/superset/Keycloak/keycloak_settings.json'
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

SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=2).total_seconds())
CUSTOM_VIEWER_FILTER = [LegalView, RGPDView]
