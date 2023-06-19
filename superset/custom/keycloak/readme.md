Pour activer l'integration de keycloak avec Superset, il faut :

1. mettre à jour keycloak_settings.json

2. rajouter ces lignes à superset_config.py

```python
from flask_appbuilder.security.manager import AUTH_OID
from superset.custom.keycloak.security_manager import OIDCSecurityManager

AUTH_TYPE = AUTH_OID
OIDC_CLIENT_SECRETS = r'/path/to/keycloak_settings.json'
OIDC_ID_TOKEN_COOKIE_SECURE = False
OIDC_REQUIRE_VERIFIED_EMAIL = False
CUSTOM_SECURITY_MANAGER = OIDCSecurityManager
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Public'
OIDC_SCOPES = ['openid']
```


