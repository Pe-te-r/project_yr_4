from flask import Flask
from .config import DevelopmentConfig
from .blueprint_module import blueprint

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    app.register_blueprint(blueprint)

    # Initialize other extensions if needed
    # e.g., db.init_app(app)

    return app
