from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from my_app.models import db
from config import DevelopmentConfig
from my_app.models import User
from my_app.routes import register_blueprints

login_manager = LoginManager()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.by_id(user_id)

    Migrate(app, db)

    # Register Blueprints
    register_blueprints(app)

    return app
