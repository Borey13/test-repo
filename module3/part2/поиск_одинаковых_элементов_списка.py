my_list = [1, 1, 2, 5, 'hello', '23', 5, 'Hello', 'hello', 10, 2, 16, 444, '5', 5]
new_list = []

for i in my_list:
    if my_list.count(i) != 1:
        new_list.append(i)

print(new_list)

# Если нужно вывести повторяющиеся элементы только один раз

print(list(set(new_list)))
