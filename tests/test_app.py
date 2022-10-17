import requests


class TestViews:

    def test_report(self, client):
        url = "/api/v1/report/"

        # test json format
        response = client.get(url, query_string={'format': "json"})
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"

        # test xml format
        response = client.get(url, query_string={'format': "xml"})
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/xml"





