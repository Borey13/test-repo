while True:
    password = input('Введите пароль: ')

    if len(password) > 8 and password.isalpha() == True and password.islower() == False and password.isupper() == False:
        print('Пароль принят!!!!')
        break
    else:
        print('Пароль должен быть более 8 символов, состоять из букв, включать заглавные и прописные буквы!!!')
