# from ..config import DevelopmentConfig
from flask import Flask
from config import DevelopmentConfig
from my_app.routes import register_blueprint

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    register_blueprint(app)

    # Initialize other extensions if needed
    # e.g., db.init_app(app)
    return app