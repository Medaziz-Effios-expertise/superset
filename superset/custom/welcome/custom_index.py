from flask_appbuilder import expose, IndexView
from superset.superset_typing import FlaskResponse
from flask import redirect
from superset.utils.core import get_user_id
from superset import appbuilder


class SupersetDashboardIndexView(IndexView):

    def get_user_welcome_dashboard(self):
        from superset.models.user_attributes import UserAttribute
        from superset.extensions import db
        from superset.models.dashboard import dashboard_user
        from sqlalchemy import select

        welcome_dashboard_id = db.session.query(
            UserAttribute.welcome_dashboard_id).filter_by(user_id=get_user_id()).scalar()
        if welcome_dashboard_id:
            return welcome_dashboard_id

        query = select([dashboard_user.c.dashboard_id]).where(
            dashboard_user.c.user_id == get_user_id())
        dashboard_ids = db.session.execute(query)
        if dashboard_ids:
            return dashboard_ids.scalar()

    @expose("/")
    def index(self) -> FlaskResponse:
        user_id = get_user_id()
        if user_id is None:
            return redirect(appbuilder.get_url_for_login)
        else:
            welcome_dashboard = self.get_user_welcome_dashboard()
            if welcome_dashboard:
                return redirect(f"/superset/dashboard/{str(welcome_dashboard)}")
            else:
                return redirect("/dashboard/list/")
