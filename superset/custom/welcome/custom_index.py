from flask_appbuilder import expose, IndexView
from superset.superset_typing import FlaskResponse
from flask import redirect
from superset.utils.core import get_user_id
from superset import appbuilder


class SupersetDashboardIndexView(IndexView):

    def get_user_welcome_dashboard(self):
        from superset.models.user_attributes import UserAttribute
        from superset.extensions import db
        from superset.models.dashboard import Dashboard

        dashboard_slug = db.session.query(Dashboard.slug).\
            join(UserAttribute, UserAttribute.welcome_dashboard_id == Dashboard.id).\
            filter(UserAttribute.user_id == get_user_id()).\
            scalar()
        accueil_dashboard = db.session.query(
            Dashboard.slug).filter_by(slug="accueil").scalar()
        return dashboard_slug, bool(accueil_dashboard)

    @expose("/")
    def index(self) -> FlaskResponse:
        user_id = get_user_id()
        if user_id is None:
            return redirect(appbuilder.get_url_for_login)
        else:
            welcome_dashboard, accueil_dashboard = self.get_user_welcome_dashboard()
            view_mode = "?standalone=2"
            if welcome_dashboard:
                return redirect(f"/superset/dashboard/{welcome_dashboard}/{view_mode}")
            elif accueil_dashboard:
                return redirect(f"/superset/dashboard/accueil/{view_mode}")
            else:
                return redirect("/dashboard/welcome/")
