import array

a = array.array('i', [99, 34, 56, 78, 13, 1308, 3, 15, 9, 98, 0, 5, -89])


def sort_insert(iterable):
    for i in range(1, len(iterable)):
        tmp = iterable[i]
        while tmp < iterable[i - 1] and i > 0:
            iterable[i] = iterable[i - 1]
            iterable[i - 1] = tmp
            i -= 1

    return iterable


print(sort_insert(a))
