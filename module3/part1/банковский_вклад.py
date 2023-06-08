import math

x = float(input("Введите первоначальную сумму: "))
p = float(input("Введите процентную ставку: "))
y = float(input("Введите желаемую сумму: "))

count = 0

while x < y:
    x = math.trunc(x + x * p / 100)
    count += 1

print("Желанная сумма у Вас накопится через:", count, "лет")
