n = int(input("Введите какое количество раз необходимо повторить фразу: "))

count = 0
num = 1

while True:
    if count == n:
        break
    else:
        print(num, "цикл For - частный случай цикла While")
        count += 1
        num += 1
