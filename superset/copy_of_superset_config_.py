from flask_appbuilder.security.manager import AUTH_OID
from superset.Keycloak.security_manager import OIDCSecurityManager

AUTH_TYPE = AUTH_OID
OIDC_CLIENT_SECRETS = r'C:\Users\ladha\PycharmProjects\superset\superset\Keycloak\keycloak_settings.json'
OIDC_ID_TOKEN_COOKIE_SECURE = False
OIDC_REQUIRE_VERIFIED_EMAIL = False
CUSTOM_SECURITY_MANAGER = OIDCSecurityManager
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
SQLALCHEMY_DATABASE_URI = 'postgresql://MedazizLad:admin@localhost/superset'

LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "fr": {"flag": "fr", "name": "Français"},
}

APP_NAME = "EFFIOS_SUPERSET"
APP_ICON = "/static/assets/images/ministry_logo.png"
LOGO_TARGET_PATH = '/'
FAVICONS = [{"href": "/static/assets/images/ministry_logo.ico"}]
