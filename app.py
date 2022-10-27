from pathlib import Path

from flask import Flask, current_app
from flask_restful import Api
from flasgger import Swagger

from api import DriversList


def create_app():
    app = Flask(__name__)
    app.config["PATH"] = Path(__file__).parent/"separate folder"
    Swagger(app)
    create_api(app)

    return app


def create_api(app):
    api = Api(app)

    api.add_resource(DriversList, '/api/v1/report/')
    api.init_app(app)
    return api


if __name__ == '__main__':  # pragma no cover
    create_app().run(debug=True)

