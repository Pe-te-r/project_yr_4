from flask import Flask, jsonify
from flask_migrate import Migrate
from my_app.models import db
from config import DevelopmentConfig
from my_app.routes import register_blueprints

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    Migrate(app,db)

    # Register Blueprints
    register_blueprints(app)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'hello user'})


    return app
