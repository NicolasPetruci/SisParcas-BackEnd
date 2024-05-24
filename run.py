from src.main.configs import create_app, config_dict
from decouple import config

DEBUG = config("DEBUG", default=True, cast=bool)

config_mode = "Development" if DEBUG else "Production"


try:
    app_config = config_dict[config_mode.capitalize()]
except KeyError:
    exit("ERROR: INVALID CONFIG")

app = create_app(app_config)

if DEBUG:
    app.logger.info("Environment = "+ config_mode)
    app.logger.info("SRC         = "+ app_config.basedir)

if __name__ == "__main__":
    app.run()