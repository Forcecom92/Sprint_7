import allure
import pytest
import requests
import urls
from data import TestDataBody

class TestMakeOrder:
    @allure.title('Проверяем создание заказа')
    @allure.description('Проверям возможность совершения заказа с доступным выбором цветов с помощью параметризации. В ответ ждем код 201 и слово track в теле ответа')
    @pytest.mark.parametrize(TestDataBody.params_order_keys, TestDataBody.params_order_values)
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, colour):
        payload = {'firstName': firstName, 'lastName': lastName, 'address': address,
                   'metroStation': metroStation, 'phone': phone, 'rentTime': rentTime,
                   'deliveryDate': deliveryDate, 'comment': comment, 'colour': colour}
        response = requests.post(urls.URL_BASE + urls.URL_CREATE_ORDER, json = payload)
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Проверка получения списка заказов')
    @allure.description('Получаем список заказов без id курьера и ждем код 200 с непустым списком заказа')
    def test_get_list_orders(self):
        response = requests.get(urls.URL_BASE + urls.URL_GET_ALL_ORDERS)
        assert response.status_code == 200 and response.json()["orders"] is not None