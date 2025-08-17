import random
import string
import allure

class TestMethodHelper:
    @staticmethod
    @allure.step('Создание рандомных регистрационных данных')
    def register_new_courier_and_return_login_password():

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string


        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        login_pass = {"login": login, "password": password, "firstName": first_name}
        return login_pass