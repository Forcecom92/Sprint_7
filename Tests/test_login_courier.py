import requests
import urls
import allure
import helper
from data import TestDataBody


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверяем, что происходит успешная аворизация курьера с кодом ответа 200 и приходит не пустой id')
    def test_success_login(self, default_courier):
        payload = default_courier
        requests.post(urls.URL_BASE + urls.URL_CREATE_COURIER, data=payload)
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data=payload)
        assert response.status_code == 200 and response.json()["id"] is not None

    @allure.title('Авторизация курьера с неправильными данными')
    @allure.description('Передаем, что нельзя залогиниться без логина, что приходит ожидаемый статус 400 и соответствующее письменное уведомление')
    def test_login_with_empty_data(self):
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data= TestDataBody.BODY_WITHOUT_LOGIN)
        assert response.status_code == 400 and response.json()["message"] == TestDataBody.login_wrong_login_400_text

    @allure.title('Авторизация курьера с несуществующими данными')
    @allure.description('Проверяем, что нельзя залогиниться несуществующими курьером и что приходит ответ 404 с соответствующим письменным уведомлением')
    def test_login_without_registration(self):
        payload = helper.TestMethodHelper.register_new_courier_and_return_login_password()
        response = requests.post(urls.URL_BASE + urls.URL_LOGIN, data = payload)
        assert response.status_code == 404 and response.json()["message"] == TestDataBody.login_wrong_login_404_text
