from flask import Flask
from flask_restful import Api
from handlers.api import DriversList
from flasgger import Swagger
from flask import make_response
import json
from simplexml import dumps



def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    create_swagger(app)
    create_api(app)

    return app


def create_swagger(app):
    app.config["SWAGGER"] = {
        'title': 'Drivers List',
        'doc_dir': './examples/docs/'
    }
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
