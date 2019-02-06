from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    from app.api_1 import bp as api_1_bp
    app.register_blueprint(api_1_bp, url_prefix= '/api/v1')

    return app

