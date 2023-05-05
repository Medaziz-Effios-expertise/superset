from flask_appbuilder import expose
from flask_babel import gettext as _
from superset.views.base import BaseSupersetView

# Define the LegalView class


class LegalView(BaseSupersetView):
    route_base = "/legal"

    @expose("/")
    def index(self):
        return self.render_template(
            "templates/superset/custom/legal.html",
            title=_("Mentions légales").__str__(),
        )

# Define the RGPDView class


class RGPDView(BaseSupersetView):
    route_base = "/rgpd"

    @expose("/")
    def index(self):
        return self.render_template(
            "templates/superset/custom/rgpd.html",
            title=_("Mentions RGPD").__str__(),
        )
