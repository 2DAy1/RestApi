from flask import jsonify, make_response, config, current_app, Blueprint
from flask_restful import Resource, request
from report_of_monaco_2018_racing_dan import report
from dicttoxml import dicttoxml
from flasgger import swag_from


class DriversList(Resource):
    @staticmethod
    def get_drivers(path):
        drivers = {}
        for driver in report.create_drivers(path):
            drivers[driver.code] = {
                "number":
                    driver.number,
                "name":
                    driver.name,
                "company":
                    driver.company,
                "result":
                    driver.result
            }
        return drivers

    @swag_from('static/drivers.yml')
    def get(self):
        path = current_app.config.get("INFO")
        DRIVERS = DriversList.get_drivers(path)

        lis_format = request.args.get('format')
        order = request.args.get('order')
        if lis_format or order:
            drivers = DRIVERS
            if order == "ask":
                drivers = dict(list(DRIVERS.items())[::-1])
            if lis_format == 'xml':
                d = dicttoxml(drivers)
                response = make_response(d)
                response.headers['content-type'] = 'application/xml'
            elif lis_format == 'json':
                d = jsonify(drivers)
                response = make_response(list(d))
                response.headers["Content-Type"] = "application/json"
            return response
