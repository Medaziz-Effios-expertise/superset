from superset.views.base_api import BaseSupersetApi
from flask_appbuilder.api import expose, protect, safe, Response
from superset.views.base_api import statsd_metrics
from flask_appbuilder.security.decorators import has_access
from superset.models.user_attributes import UserAttribute
from superset.utils.core import get_user_id
from superset import db


class CustomRestApi(BaseSupersetApi):

    @expose("/welcome_dashboard/<int:dashboard_id>", methods=["POST"])
    @protect(allow_browser_login=True)
    @safe
    @statsd_metrics
    @has_access
    def set_user_welcome_dashboard(self, dashboard_id: int) -> Response:
        try:
            user_id = get_user_id()
            user_attribute = db.session.query(
                UserAttribute).filter_by(user_id=get_user_id()).scalar()
            if user_attribute:
                user_attribute.welcome_dashboard_id = dashboard_id
                code = 200
            else:
                user_attribute = UserAttribute(
                    user_id=user_id,
                    welcome_dashboard_id=dashboard_id
                )
                db.session.add(user_attribute)
                code = 201

            db.session.commit()
            return self.response(code, message='Set to welcome dashboard succesfuly')
        except Exception as ex:
            db.session.rollback()
            return self.response(500, message=str(ex))

    @expose("/welcome_dashboard/", methods=["GET"])
    @protect(allow_browser_login=True)
    @safe
    @statsd_metrics
    @has_access
    def get_default_dashboard(self) -> Response:
        user_id = get_user_id()
        user_attributes = db.session.query(
            UserAttribute).filter_by(user_id=user_id).scalar()
        if user_attributes:
            dashboard_id = user_attributes.welcome_dashboard_id
        else:
            dashboard_id = None

        response_data = {
            'dashboard_id': dashboard_id
        }
        return self.response(200, result=response_data)
