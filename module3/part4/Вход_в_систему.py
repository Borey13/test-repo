import json


def login_function():
    with open("login_and_password.json", "r") as f:
        all_data = json.load(f)
    while True:
        user_login = input("Введите логин :")
        if user_login not in all_data.keys():
            user_password = input("Введите пароль :")
            all_data[user_login] = user_password
            with open("login_and_password.json", "w") as f:
                json.dump(all_data, f)
            print("Вы успешно зарегистрированы!!!")
            break
        else:
            while True:
                user_password = input("Введите пароль :")
                if all_data[user_login] == user_password:
                    print("Вы усппешно вошли в систему!!!")
                    break
                else:
                    print("Пароль неверный, попробуйте снова!!!")
