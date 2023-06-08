num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))

num_max = (num1 > num2) * num1 + (num2 >= num1) * num2
print('максимальное число: ', num_max)
