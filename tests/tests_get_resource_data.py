import httpx
from  jsonschema import validate

from core.contracts import RESOURCE_DATA_SCHEME

base_url = "https://reqres.in/"
resource = "api/unknown"


def test_list_resource():
    response = httpx.get(base_url + resource)
    assert response.status_code == 200
    data = response.json()["data"]

    for el in data:
        validate(el, RESOURCE_DATA_SCHEME)
        assert '#' in el["color"]
        assert type(el["year"]) == int

def test_single_resource():
    response = httpx.get(base_url + resource + "/2") #мне стало лень делать отдельнкую переменную
    assert response.status_code == 200
    data = response.json()["data"]

    validate(data, RESOURCE_DATA_SCHEME)
    assert '#' in data["color"]
    assert type(data["year"]) == int

def test_single_resource_404():
    response = httpx.get(base_url + resource + "/23") #мне стало лень делать отдельнкую переменную
    assert response.status_code == 404
