x = int(input('Введите первре число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

count = 1

if x == y and x == z:
    print(3)
elif x == y or y == z or x == z:
    print(2)
else:
    print(0)
