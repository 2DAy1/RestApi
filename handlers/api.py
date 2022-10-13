from flask import jsonify
from flask_restful import Resource, abort, reqparse, request
from report_of_monaco_2018_racing_dan import report
from dict2xml import dict2xml


class DriversList(Resource):
    DRIVERS = {}

    for driver in report.create_drivers():
        DRIVERS[f"driver {driver.number}"] = {
            driver.code:
                {
                    "number": driver.number,
                    "name": driver.name,
                    "company": driver.company,
                    "resul": driver.result
                }
        }



    def get(self):
        if request.args.get('format') == 'json':
            resp = jsonify(DriversList.DRIVERS)
            return resp, 200

        elif request.args.get('format') == 'xml':
            xml = dict2xml(DriversList.DRIVERS)
            return xml, 200
