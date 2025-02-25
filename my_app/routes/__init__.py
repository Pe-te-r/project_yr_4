from my_app.routes.auth import auth_bp
from my_app.routes.home import home_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='')
    app.register_blueprint(home_bp, url_prefix='')