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

        # test order
        response_desc = client.get(url, query_string={'order': "ask"})
        response_ask = client.get(url, query_string={'order': "ask"})
        assert response_ask.status_code == 200
        assert response_desc.status_code == 200
        assert response_ask.text == response_desc.text[:1]



