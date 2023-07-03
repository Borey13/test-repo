import array

a = array.array('i', [12, 34, 56, 78, 89, 100, 123, 145, 167, 198, 205])


def binary_search(iterable, value):
    left = 0
    right = len(iterable) - 1

    while right >= left:
        mid = (left + right) // 2

        if iterable[mid] == value:
            return True

        if iterable[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return False


print(binary_search(a, 123))
