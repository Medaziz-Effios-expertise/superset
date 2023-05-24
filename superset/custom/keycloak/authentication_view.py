import logging
from flask import redirect, g, session
from flask_appbuilder import expose
from flask_appbuilder.security.views import AuthOIDView
from flask_login import login_user
import requests
import urllib.parse


class AuthOIDCView(AuthOIDView):

    @expose('/login/', methods=['GET', 'POST'])
    def login(self):
        sm = self.appbuilder.sm
        oidc = sm.oid
        logger = logging.getLogger(__name__)

        @self.appbuilder.sm.oid.require_login
        def handle_login():
            email = oidc.user_getfield('email')
            user = sm.auth_user_oid(email)
            infos = oidc.user_getinfo(
                ['preferred_username', 'given_name', 'family_name', 'email'])
            client_id = oidc.client_secrets['client_id']
            default_role = sm.find_role('Public')
            roles = g.oidc_id_token.get('realm_access', {}).get('roles', [])
            resource_roles = g.oidc_id_token.get(
                'resource_access', {}).get(client_id, {}).get('roles', [])
            roles.extend(resource_roles)

            user_roles = []

            if roles:
                for role_name in roles:
                    role = sm.find_role(role_name)
                    if role:
                        user_roles.append(role)
                    else:
                        logger.warning(
                            f"Role '{role_name}' in Keycloak does not exist in Superset")
                        continue
            if not roles:
                user_roles.append(default_role)
            if not user:
                user = sm.add_user(
                    infos['preferred_username'],
                    infos['given_name'],
                    infos['family_name'],
                    infos['email'],
                    user_roles
                )
            else:
                user.roles = user_roles
                user.username = infos['preferred_username']
                user.first_name = infos['given_name']
                user.last_name = infos['family_name']
                user.email = infos['email']
                sm.update_user(user)

            login_user(user, remember=False)
            return redirect(self.appbuilder.get_url_for_index)
        return handle_login()

    @expose('/logout', methods=['GET', 'POST'])
    def logout(self):
        oidc = self.appbuilder.sm.oid
        logger = logging.getLogger(__name__)
        logout_url = 'http://winhost:8080/realms/Superset-EFFIOS/protocol/openid-connect/logout'
        client_id = oidc.client_secrets['client_id']
        client_secret = oidc.client_secrets['client_secret']
        refresh_token = oidc.get_refresh_token()
        access_token = oidc.get_access_token()
        oidc.logout()
        session.clear()
        super(AuthOIDCView, self).logout()
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': refresh_token
        }
        encoded_data = urllib.parse.urlencode(data)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + access_token
        }

        response = requests.post(
            logout_url, data=encoded_data, headers=headers)
        if response.status_code == 204:
            logger.info('Keycloak Logout successful.')
        else:
            logger.warning('Logout failed. Status code:', response.status_code)

        return super(AuthOIDCView, self).logout()
