import sys

from flask import Flask
from flask_restful import Api
from handlers.api import DriversList
from flasgger import Swagger
from flask import make_response
import json
from simplexml import dumps
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    create_swagger(app)
    create_api(app)

    return app


def create_swagger(app):
    ### swagger specific ###
    SWAGGER_URL = '/swagger'
    API_URL = '/static/drivers.yml'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### end swagger specific ###

    swagger = Swagger(app)

    return swagger


def create_api(app):
    api = Api(app)

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        resp = make_response(json.dumps({data}), code)
        resp.headers.extend(headers or {})
        return resp


    @api.representation('application/xml')
    def output_xml(data, code, headers=None):
        resp = make_response(dumps({'response': data}), code)
        resp.headers.extend(headers or {})
        return resp


    api.add_resource(DriversList, '/api/v1/report/')
    api.init_app(app)
    return api


if __name__ == '__main__':  # pragma no cover
    create_app().run(debug=True)
