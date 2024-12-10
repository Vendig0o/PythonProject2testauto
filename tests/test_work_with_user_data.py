import datetime
from http.client import responses

import httpx
from  jsonschema import validate
import allure
from core.contracts import *

base_url = "https://reqres.in/"
create_user = "api/users"
change_user = "api/users/2"

def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    response = httpx.post(base_url + create_user,json=body)
    with allure.step("Проверям статус код == 200"):
        assert response.status_code == 201
    response_json = response.json()
    creation_date = response_json["createdAt"].replace("T"," ")
    current_date = str(datetime.datetime.utcnow())

    validate(response_json, CREATE_USER_DATA_SCHEME)
    assert response_json['name'] == body['name']
    assert response_json['job'] == body['job']
    assert creation_date[0:16] == current_date[0:16]

# основное ДЗ ниже

@allure.suite("Проверка изменений информации о пользователе")
@allure.title("Проверка обновления пользователя через PUT")
def test_put_update_user():
    body = {
        "name": "Monster",
        "job": "Qa"
    }
    with allure.step("Отправляем запрос на обновление пользователя Put"):
        response = httpx.put(base_url + change_user,json=body)
    with allure.step("Проверям статус код == 200"):
        assert response.status_code == 200
    response_json = response.json()
    updated_date = response_json["updatedAt"].replace("T"," ")
    current_date = str(datetime.datetime.utcnow())
    with allure.step("Проводим валидацию согласно схеме"):
        validate(response_json, UPDATE_USER_DATA_SCHEME)
    with allure.step("Проверяем корректность обновления имени"):
        assert response_json['name'] == body['name']
    with allure.step("Проверяем корректность обновления должности"):
        assert response_json['job'] == body['job']
    with allure.step("Проверям корректность записанной даты обновления"):
        assert updated_date[0:16] == current_date[0:16]

@allure.suite("Проверка изменений информации о пользователе")
@allure.title("Проверка обновления пользователя через Patch")
def test_patch_update_user():
    body = {
        "name": "Monster",
        "job": "Qa"
    }
    with allure.step("Отправляем запрос на обновление пользователя Patch"):
        response = httpx.patch(base_url + change_user,json=body)
    with allure.step("Проверям статус код == 200"):
        assert response.status_code == 200
    response_json = response.json()
    updated_date = response_json["updatedAt"].replace("T"," ")
    current_date = str(datetime.datetime.utcnow())

    with allure.step("Проводим валидацию согласно схеме"):
        validate(response_json, UPDATE_USER_DATA_SCHEME)
    with allure.step("Проверяем корректность обновления имени"):
        assert response_json['name'] == body['name']
    with allure.step("Проверяем корректность обновления должности"):
        assert response_json['job'] == body['job']
    with allure.step("Проверям корректность записанной даты обновления"):
        assert updated_date[0:16] == current_date[0:16]

@allure.suite("Проверка изменений информации о пользователе")
@allure.title("Проверкак удаления пользователя")
def test_delete_user():
    with allure.step("Дергаем метод удаления пользователя"):
        response = httpx.delete(base_url + change_user)
    with allure.step("Проверям статус код == 204"):
        assert response.status_code == 204