from flask import Flask
from config import config
from flask.ext.heroku import Heroku

def create_app(config_name):
    app = Flask(__name__)
    heroku = Heroku(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


    from app.api_1 import bp as api_1_bp
    app.register_blueprint(api_1_bp, url_prefix= '/api/v1')

    from app.api_2 import bp2 as api_2_bp
    app.register_blueprint(api_2_bp, url_prefix = '/api/v2')
    return app

