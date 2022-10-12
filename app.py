from flask import Flask
from flask_restful import Api
from handlers.api import DriversList


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    create_api(app)

    return app


def create_api(app):
    api = Api(app)
    api.add_resource(DriversList, '/api/v1/report')
    api.init_app(app)
    return api


if __name__ == '__main__':  # pragma no cover
    create_app().run(debug=True)
