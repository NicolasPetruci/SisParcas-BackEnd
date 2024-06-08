from flask import Flask
from flask_cors import CORS
from importlib import import_module

def register_blueprints(app: Flask):
    routes: tuple = (
        "default",
        "cargo_routes",
        "usuario_routes",
        "evento_routes",
        "rpg_routes",
    )
    for blueprint in routes:
        module = import_module("src.main.routes.{}".format(blueprint))
        app.register_blueprint(module.blueprint)

def create_app(config)->Flask:
    app: Flask = Flask(__name__) 
    app.config.from_object(config)
    cors = CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    register_blueprints(app)
    return app

