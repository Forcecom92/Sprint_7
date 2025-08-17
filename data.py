class TestDataBody:

    BODY_WITHOUT_LOGIN = {"login": "",
                          "password": "333222111",
                          "firstName": "Якобс Монарх"}

    courier_wrong_login_400_text =  "Недостаточно данных для создания учетной записи"
    courier_wrong_login_409_text = "Этот логин уже используется"
    login_wrong_login_400_text = "Недостаточно данных для входа"
    login_wrong_login_404_text = "Учетная запись не найдена"

    params_order_keys = 'firstName, lastName, address, metroStation, phone, deliveryDate, rentTime, comment, colour'
    params_order_values = [
        ["Dart", "Weider", "Tatooine, 407 apt", 4, "+7 800 355 35 35", 5, "2025-09-06", "печенек", ["BLACK"]],
        ["Naruto", "Uchiha", "Konoha, 142 apt.", 4, "+7 800 355 35 35", 5, "2025-09-06", "страданий", ["BLACK", "GREY"]],
        ["Harry", "Potter", "Litte Winging, 4", 4, "+7 800 355 35 35", 5, "2025-09-06", "метлу", []]
    ]
