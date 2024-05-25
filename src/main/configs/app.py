from flask import Flask
from importlib import import_module
from .errors import handle_400, handle_404, handle_405, handle_500

def register_errors(app: Flask):
    app.register_error_handler(400, handle_400)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(405, handle_405)
    app.register_error_handler(500, handle_500)

def register_blueprints(app: Flask):
    routes: tuple = (
        "default",
        "cargo_routes"
    )
    for blueprint in routes:
        module = import_module("src.main.routes.{}".format(blueprint))
        app.register_blueprint(module.blueprint)

def create_app(config)->Flask:
    app: Flask = Flask(__name__)   
    app.config.from_object(config)
    register_blueprints(app)
    register_errors(app)
    return app

