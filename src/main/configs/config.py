import uuid
from os import path

key = str(uuid.uuid4())

class Config(object):
    SECRET_KEY = key
    basedir = path.abspath(path.join(__file__, "../../.."))

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

config_dict = { "Development": DevelopmentConfig, 'Production': ProductionConfig }