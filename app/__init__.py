from flask import Flask, jsonify
from config import config
from flask.ext.heroku import Heroku

def error_response(status_code, message = None):
    payload = {
        "status": status_code,
        "error" : message
    }
    response = jsonify(payload)
    response.status_code = status_code
    return response

def not_found(e):
    return error_response(404, "No such url found")

def bad_request(e):
    return error_response(400, "Bad request, invalid json format")

def invalid_method(e):
    return error_response(405, "Method not allowed")

def create_app(config_name):
    app = Flask(__name__)
    heroku = Heroku(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    app.register_error_handler(404, not_found)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(405, invalid_method)
    from app.api_1 import bp as api_1_bp
    app.register_blueprint(api_1_bp, url_prefix= '/api/v1')

    from app.api_2 import bp2 as api_2_bp
    app.register_blueprint(api_2_bp, url_prefix = '/api/v2')
    return app

