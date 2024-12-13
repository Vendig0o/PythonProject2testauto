from http.client import responses
import httpx
import json
import pytest
from jsonschema import validate
from core.contracts import REGISTER_AND_LOGIN_USER_DATA_SCHEME
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, '..', 'core', 'register_and_login_users_data.json')
json_file = open(file_path)

base_url = "https://reqres.in/"
register_user = "api/register"
login_user = "api/login"
users_data = json.load(json_file)


@pytest.mark.parametrize('users_data', users_data)
def test_successful_register(users_data):
    response = httpx.post(base_url + register_user, json=users_data)
    assert response.status_code == 200

@pytest.mark.parametrize('email', [user['email'] for user in users_data])
def test_unsuccessful_register(email):
    data = {'email': email}
    response = httpx.post(base_url + register_user, json=data)
    assert response.status_code == 400

@pytest.mark.parametrize('users_data', users_data)
def test_successful_login(users_data):
    response = httpx.post(base_url + login_user, json=users_data)
    assert response.status_code == 200

@pytest.mark.parametrize('email', [user['email'] for user in users_data])
def test_unsuccessful_login(email):
    data = {'email': email}
    response = httpx.post(base_url + login_user, json=data)
    assert response.status_code == 400