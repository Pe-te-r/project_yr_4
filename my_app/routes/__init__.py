def register_blueprint(app):
    from my_app.routes.auth import a
    app.register_blueprint()