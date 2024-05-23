from flask import Flask
from importlib import import_module


def register_blueprints(app: Flask):
    routes: tuple = (
        "default",
    )
    for blueprint in routes:
        module = import_module("src.main.routes.{}".format(blueprint))
        app.register_blueprint(module.blueprint)

def create_app(config)->Flask:
    app: Flask = Flask(__name__)   
    app.config.from_object(config)
    register_blueprints(app)
    return app

