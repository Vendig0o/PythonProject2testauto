import httpx
from  jsonschema import validate
import allure
from core.contracts import RESOURCE_DATA_SCHEME

base_url = "https://reqres.in/"
resource = "api/unknown"

@allure.suite("Проверка запроса ресурсов")
@allure.title("Проверяем получение списка ресурсов")
def test_list_resource():
    with allure.step("Делаем запрос к списку ресурсов"):
        response = httpx.get(base_url + resource)
    with allure.step("Проверяем статус код == 200"):
        assert response.status_code == 200
    data = response.json()["data"]

    for el in data:
        with allure.step("Проверяем каждый элемент списка"):
            validate(el, RESOURCE_DATA_SCHEME)
            with allure.step("Проверяем что цвет начинается с #"):
                assert '#' in el["color"]
            with allure.step("Проверяем что год четырехзначный"):
                assert len(str(el["year"])) == 4


@allure.suite("Проверка запроса ресурсов")
@allure.title("Проверяем получение одиночного ресурса")
def test_single_resource():
    with allure.step("Делаем запрос к определенному ресурсу"):
        response = httpx.get(base_url + resource + "/2") #мне стало лень делать отдельнкую переменную
    with allure.step("Проверяем статус код == 200"):
        assert response.status_code == 200
    data = response.json()["data"]

    validate(data, RESOURCE_DATA_SCHEME)
    with allure.step("Проверяем что цвет начинается с #"):
        assert '#' in data["color"]
    with allure.step("Проверяем что год четырехзначный"):
        assert len(str(data["year"])) == 4


@allure.suite("Проверка запроса ресурсов")
@allure.title("Получаем 404 по поиску ресурса")
def test_single_resource_404():
    with allure.step("Делаем запрос к несуществующему ресурсу"):
        response = httpx.get(base_url + resource + "/23") #мне стало лень делать отдельнкую переменную
    with allure.step("Проверяем статус код == 404"):
        assert response.status_code == 404
