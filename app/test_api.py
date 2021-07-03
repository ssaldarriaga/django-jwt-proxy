import pytest
from fastapi.testclient import TestClient
from mock import patch
from pytest_httpx import HTTPXMock

from app.main import app
from app.utils import decode_jwt
from app.settings import TARGET_BASE_URL_API, JWT_HEADER

client = TestClient(app)

@pytest.mark.describe("/api/users - Request body validation")
def test_should_returns_422_when_body_is_empty():
    response = client.post("/api/users")
    assert response.status_code == 422

@pytest.mark.describe("/api/users - Request body validation")
def test_should_returns_400_when_username_is_empty():
    response = client.post("/api/users", json={"name": "", "job": "fake-job"})
    assert response.status_code == 400
    assert response.json()["detail"] == "The username can not be empty"

@pytest.mark.describe("/api/users - Request body validation")
def test_should_returns_400_when_job_is_empty():
    response = client.post("/api/users", json={"name": "fake-username", "job": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "The job can not be empty"

@pytest.mark.describe("/api/users - Request to target API")
def test_should_create_a_user_successfully(httpx_mock: HTTPXMock):
    url = "{base}/api/users".format(base=TARGET_BASE_URL_API)
    json = {"username": "fake-username"}
    httpx_mock.add_response(url=url, method="POST", json=json)

    response = client.post("/api/users", json={"name": "fake-username", "job": "fake-job"})
    assert response.status_code == 200
    assert response.json() == json

@pytest.mark.describe("/api/users - Request to target API")
def test_should_includes_jwt_header(httpx_mock: HTTPXMock):
    url = "{base}/api/users".format(base=TARGET_BASE_URL_API)
    httpx_mock.add_response(url=url, method="POST")
    response = client.post("/api/users", json={"name": "fake-username", "job": "fake-job"})
    headers_keys = list(httpx_mock.get_request().headers.keys())
    assert JWT_HEADER in headers_keys

@pytest.mark.describe("/api/users - Request to target API")
def test_jwt_data_should_matches_with_expected_data(httpx_mock: HTTPXMock):
    url = "{base}/api/users".format(base=TARGET_BASE_URL_API)
    httpx_mock.add_response(url=url, method="POST")

    with patch("app.utils.get_now_timestamp", return_value=100000000.0001):
        with patch("app.utils.get_now", return_value="2021-07-02 23:17:11.360749"):
            response = client.post("/api/users", json={"name": "fake-username", "job": "fake-job"})

    expected_jwt_data = {
        'iat': 100000000, 
        'jti': '2186355435e85837c6422bf91bbf78e1', 
        'payload': {'username': 'fake-username', 'date': '2021-07-02 23:17:11.360749'}
    }

    jwt = httpx_mock.get_request().headers.get("x-my-jwt")
    jwt_data = decode_jwt(jwt)
    assert jwt_data == expected_jwt_data