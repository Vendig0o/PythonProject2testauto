import allure

import httpx
from  jsonschema import validate

from core.contracts import USER_DATA_SCHEME

base_url = "https://reqres.in/"
list_users = "api/users?page=2"
email_ends = "@reqres.in"
single_user = "api/users/2"

@allure.suite("Проверка запроса пользователей")
@allure.title("Проверка получения списка пользователей")
def test_list_users():
    with allure.step("Делаем запрос к списку пользователей"):
        response = httpx.get(base_url + list_users)
    with allure.step("Проверяем статус код == 200"):
        assert response.status_code == 200

    data = response.json()["data"]

    for el in data:
        with allure.step("Проверяем каждый элемент списка"):
            validate(el, USER_DATA_SCHEME)
            with allure.step("Проверяем окончание почты"):
                assert el["email"].endswith(email_ends)
            with allure.step("Проверяем наличие id в avatar"):
                assert str(el["id"]) in el["avatar"]

@allure.suite("Проверка запроса пользователей")
@allure.title("Проверка получения одиночного пользователя")
def test_single_user():
    with allure.step("Делаем запрос к определенному пользователю"):
        response = httpx.get(base_url + single_user)
    with allure.step("Проверяем статус код == 200"):
        assert response.status_code == 200

    data = response.json()["data"]

    validate(data, USER_DATA_SCHEME)
    with allure.step("Проверяем окончание почты"):
        assert data["email"].endswith(email_ends)
    with allure.step("Проверяем наличие id в avatar"):
        assert str(data["id"]) in data["avatar"]


@allure.suite("Проверка запроса пользователей")
@allure.title("Получаем 404 по поиску пользователя")
def test_single_user_404():
    with allure.step("Делаем запрос к несуществующему пользователю"):
        response = httpx.get(base_url + single_user + "3") #мне стало лень делать отдельнкую переменную
    with allure.step("Проверяем статус код == 404"):
        assert response.status_code == 404