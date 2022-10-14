from flask import jsonify, make_response
from flask_restful import Resource, request
from report_of_monaco_2018_racing_dan import report
from dicttoxml import dicttoxml


class DriversList(Resource):
    DRIVERS = {}

    for driver in report.create_drivers():
        DRIVERS[f"driver{driver.number}"] = {
            driver.code:
                {
                    "number":
                    driver.number,
                    "name":
                    driver.name,
                    "company":
                    driver.company,
                    "resul":
                    driver.result
                }
        }

    def get(self):
        if request.args.get('format') == 'xml':
            d = dicttoxml(DriversList.DRIVERS)
            response = make_response(d)
            response.headers['content-type'] = 'application/xml'

        elif request.args.get('format') == 'json':
            d = jsonify(DriversList.DRIVERS)
            response = make_response(d)
            response.headers["Content-Type"] = "application/json"

        return response
