

import httpx
from  jsonschema import validate

from core.contracts import USER_DATA_SCHEME

base_url = "https://reqres.in/"
list_users = "api/users?page=2"
email_ends = "@reqres.in"

def test_list_users():
    response = httpx.get(base_url + list_users)
    assert response.status_code == 200
    data = response.json()["data"]

    for el in data:
        validate(el, USER_DATA_SCHEME)
        assert el["email"].endswith(email_ends)
        assert str(el["id"]) in el["avatar"]