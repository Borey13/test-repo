import unittest

a = [10, 5, 8, 2, 4, 1, 3, 6, 9, 7]


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)


print(merge_sort(a))
print(sorted(a))


class TestMergeSort(unittest.TestCase):
    def test1(self):
        self.assertEqual(len(merge_sort(a)), len(a))

    def test2(self):
        merge_sorted_list = merge_sort(a)
        sorted_list = sorted(a)
        for i in range(0, len(a)):
            self.assertEqual(merge_sorted_list[i], sorted_list[i])
