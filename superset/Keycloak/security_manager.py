from flask_appbuilder.security.manager import AUTH_OID
from flask_oidc import OpenIDConnect

from superset.Keycloak.authentication_view import AuthOIDCView
from superset.security import SupersetSecurityManager


class OIDCSecurityManager(SupersetSecurityManager):

    def __init__(self, appbuilder):
        super(OIDCSecurityManager, self).__init__(appbuilder)
        if self.auth_type == AUTH_OID:
            self.oid = OpenIDConnect(self.appbuilder.get_app)
        self.authoidview = AuthOIDCView
