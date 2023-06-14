import json


def registr():
    with open("login_and_password.json", "r") as f:
        all_data = json.load(f)
    while True:
        user_login = input("Введите логин: ")
        if user_login not in all_data.keys():
            break
        else:
            print("Имя пользователя занято, введите другое имя: ")

    user_password = input("Введите пароль: ")
    all_data[user_login] = user_password
    with open("login_and_password.json", "w") as f:
        json.dump(all_data, f)
    print("Вы успешно зарегистрированы!!!")
