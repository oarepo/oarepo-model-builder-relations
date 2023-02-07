import re

from referrer import config as config


class ReferrerExt:
    """referrer extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        self.resource = None
        self.service = None

        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""

        self.init_config(app)
        if not self.is_inherited():
            self.init_resource(app)
            self.register_flask_extension(app)

    def register_flask_extension(self, app):
        app.extensions["referrer"] = self

    def init_resource(self, app):
        """Initialize vocabulary resources."""
        self.service = app.config["REFERRER_SERVICE_CLASS_REFERRER"](
            config=app.config["REFERRER_SERVICE_CONFIG_REFERRER"](),
        )
        self.resource = app.config["REFERRER_RESOURCE_CLASS_REFERRER"](
            service=self.service,
            config=app.config["REFERRER_RESOURCE_CONFIG_REFERRER"](),
        )

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_]*$", identifier) and not identifier.startswith("_"):
                app.config.setdefault(identifier, getattr(config, identifier))

    def is_inherited(self):
        from importlib_metadata import entry_points

        ext_class = type(self)
        for ep in entry_points(group="invenio_base.apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        for ep in entry_points(group="invenio_base.api_apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        return False