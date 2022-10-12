from flask import jsonify
from flask_restful import Resource, abort, reqparse, request
from report_of_monaco_2018_racing_dan import report

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

# parser = reqparse.RequestParser()
# parser.add_argument('driver_code')
# parser.add_argument('number')
# parser.add_argument('name')
# parser.add_argument('company')
# parser.add_argument('result')


def abort_if_todo_doesnt_exist(driver_id):
    if driver_id not in DRIVERS:
        abort(404, message="{} doesn't exist".format(driver_id))


# class Driver(Resource):
#     def get(self, driver_id):
#         abort_if_todo_doesnt_exist(driver_id)
#         return DRIVERS[driver_id]

    # def delete(self, driver_id):
    #     abort_if_todo_doesnt_exist(driver_id)
    #     del DRIVERS[driver_id]
    #     return '', 204
    #
    # def put(self, driver_id):
    #     args = parser.parse_args()
    #     new_driver = {driver.code: args[driver.code]}
    #     DRIVERS[driver_id] = new_driver
    #     return new_driver, 201


class DriversList(Resource):
    def get(self):
        if request.args.get('format') == 'json':
            resp = jsonify(DRIVERS)
            resp.status_code = 200
            return resp

    # def post(self):
    #     args = parser.parse_args()
    #     driver_id = int(max(DRIVERS.keys()).lstrip('driver ')) + 1
    #     driver_id = 'driver %i' % driver_id
    #     DRIVERS[driver_id] = {
    #         args["driver_code"]: {
    #             f"{DRIVERS[-1].number+1}",
    #             args['name'],
    #             args["company"],
    #             args["resul"]
    #         }
    #     }
    #
    #     return DRIVERS[driver_id], 201


