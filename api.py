from flask import jsonify, make_response
from flask_restful import Resource, request
from report_of_monaco_2018_racing_dan import report
from dicttoxml import dicttoxml
from flasgger import swag_from


class DriversList(Resource):
    @staticmethod
    def get_drivers():
        drivers = {}

        for driver in report.create_drivers():
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

    DRIVERS = get_drivers()

    @swag_from('static/drivers.yml')
    def get(self):
        lis_format = request.args.get('format')
        if lis_format:
            if lis_format == 'xml':
                d = dicttoxml(DriversList.DRIVERS)
                response = make_response(d)
                response.headers['content-type'] = 'application/xml'
            elif lis_format == 'json':
                d = jsonify(DriversList.DRIVERS)
                response = make_response(d)
                response.headers["Content-Type"] = "application/json"
                return response

        order = request.args.get('order')
        if order:
            if order == "desc":
                drivers = jsonify(DriversList.DRIVERS)
            elif order == "ask":
                drivers = jsonify(DriversList.DRIVERS)
            return drivers



