import logging

from pytest import fixture
import requests


@fixture(scope="session")
def client():
    email = 'jack.bauer@mastek.com'
    url = 'http://localhost:8080/login'
    s = requests.Session()
    r = s.post(url, {"username": email, "password": "password"})
    assert r.status_code == 200
    logging.info("Returning client")
    yield s
    s.get('http://localhost:8080/logout')
    logging.info("Closed client")
