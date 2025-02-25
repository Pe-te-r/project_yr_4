from flask import Flask, render_template
from flask_migrate import Migrate
# from flask_login import LoginManager
from my_app.models import db
from config import DevelopmentConfig
from my_app.routes import register_blueprints

# login_manager = LoginManager()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'
    Migrate(app,db)

    # Register Blueprints
    register_blueprints(app)




    return app
