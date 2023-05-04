from urllib.parse import quote

from flask import redirect, request, g
from flask_appbuilder import expose
from flask_appbuilder.security.views import AuthOIDView
from flask_login import login_user


class AuthOIDCView(AuthOIDView):

    @expose('/login/', methods=['GET', 'POST'])
    def login(self, flag=True):
        sm = self.appbuilder.sm
        oidc = sm.oid

        @self.appbuilder.sm.oid.require_login
        def handle_login():
            user = sm.auth_user_oid(oidc.user_getfield('email'))
            roles = []
            default = sm.find_role('Public')
            realm_access = g.oidc_id_token.get('realm_access')
            if realm_access:
                realm_roles = realm_access.get('roles')
                if realm_roles:
                    for role_name in realm_roles:
                        role = sm.find_role(role_name)
                        if role:
                            roles.append(role)
                        else:
                            continue
                    else:
                        roles.append(default)
            if user is None:
                info = oidc.user_getinfo(
                    ['preferred_username', 'given_name', 'family_name', 'email'])
                user = sm.add_user(info.get('preferred_username'), info.get('given_name'),
                                   info.get('family_name'), info.get('email'),
                                   roles)
            else:
                if set(user.roles) != set(roles):
                    user.roles = roles
                    sm.update_user(user)
            login_user(user, remember=False)
            return redirect(self.appbuilder.get_url_for_index)

        return handle_login()

    @expose('/logout/', methods=['GET', 'POST'])
    def logout(self):
        oidc = self.appbuilder.sm.oid

        oidc.logout()
        super(AuthOIDCView, self).logout()
        redirect_url = request.url_root.strip(
            '/') + self.appbuilder.get_url_for_login

        return redirect(oidc.client_secrets.get(
            'issuer') + '/protocol/openid-connect/logout?redirect_uri=' + quote(
            redirect_url))
