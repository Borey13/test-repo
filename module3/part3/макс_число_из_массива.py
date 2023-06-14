import array as arr


def arr_in_int(arr_num):
    sorted_list_num = []

    for _ in range(len(arr_num)):
        if len(arr_num) != 1:
            max_num = arr_num[0]
        else:
            sorted_list_num.append(arr_num[-1])
            break
        for num in arr_num:
            if len(str(max_num)) != 1:
                first_digit_max_num = max_num // 10 ** (len(str(max_num)) - 1)
            else:
                first_digit_max_num = max_num
            if len(str(num)) != 1:
                first_digit_num = num // 10 ** (len(str(num)) - 1)
            else:
                first_digit_num = num
            if first_digit_max_num < first_digit_num:
                max_num = num
            elif first_digit_max_num == first_digit_num:
                if len(str(max_num)) > len(str(num)):
                    max_num = num
                elif len(str(max_num)) == len(str(num)):
                    max_num = max(max_num, num)
        sorted_list_num.append(max_num)
        arr_num.remove(max_num)

    int_num = ''

    for sorted_num in sorted_list_num:
        int_num += str(sorted_num)

    return int(int_num)


num1 = arr.array('i', [56, 9, 11, 2])
num2 = arr.array('i', [3, 81, 5])
num3 = arr.array('i', [12, 7, 9, 93, 44, 48])
print(arr_in_int(num1))
print(arr_in_int(num2))
print(arr_in_int(num3))
