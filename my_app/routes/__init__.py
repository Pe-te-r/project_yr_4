from my_app.routes.auth import auth_bp
from my_app.routes.home import home_bp
from my_app.routes.chat import chatp_bp
from my_app.routes.about import about_bp 

def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='')
    app.register_blueprint(home_bp, url_prefix='')
    app.register_blueprint(about_bp, url_prefix='')
    app.register_blueprint(chatp_bp, url_prefix='')