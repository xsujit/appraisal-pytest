import logging


class TestSample:

    def test_sample(self, client):
        response = client.get("http://api.zippopotam.us/us/90210")
        logging.info("Hello zippopotam")
        assert response.status_code == 200

    def test_appraisal(self, client):
        url = 'http://localhost:8080/appraisal'
        r = client.get(url)
        logging.info("Hello appraisal")
        assert r.status_code == 200
