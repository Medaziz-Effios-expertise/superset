from superset.extensions import appbuilder

class CustomInitializer:

    def init_views(self) -> None:
        from superset.custom.api.custom_api import CustomRestApi
        appbuilder.add_api(CustomRestApi)