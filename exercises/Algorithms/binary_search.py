import unittest

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# assertion: lst is already sorted


def binary_search(lst, elem):

    while len(lst) > 1:
        _init = 0
        _end = len(lst)
        _mid = _end/2

        if elem == lst[_mid]:
            return True
        elif elem < lst[_mid]:
            lst = lst[_init:_mid]
        else:
            lst = lst[_mid:_end]

    return False


def trinary_search(lst, elem):
    lst_init = lst[0:(len(lst) / 3)]
    lst_mid = lst[(len(lst) / 3):len(lst) - (len(lst) / 3)]
    lst_last = lst[len(lst) - (len(lst) / 3):len(lst)]

    while len(lst) >= 3:
        if elem < lst_mid[0]:
            lst = lst_init
        elif elem > lst_mid[-1]:
            lst = lst_last
        else:
            lst = lst_mid

    return True if elem in lst else False


class TestStringMethods(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search(range(1, 6), 2), True)
        self.assertEqual(binary_search(range(1, 200), 27), True)
        self.assertEqual(binary_search(range(1, 1000), 1001), False)


if __name__ == '__main__':
    unittest.main()
