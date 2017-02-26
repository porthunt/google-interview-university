import unittest


def biggest_seq(seq_list, c):
    all_lst = []
    tmp_lst = []

    for idx, elem in enumerate(seq_list):

        _sum = elem
        tmp_lst.append(elem)

        # if elem is already c, add to list
        if _sum == c:
            all_lst.append(tmp_lst)

        elif _sum < c:
            for i in range(idx + 1, len(seq_list)):

                if _sum + seq_list[i] == c:
                    tmp_lst.append(seq_list[i])
                    all_lst.append(tmp_lst)
                    tmp_lst = []
                    _sum = 0
                    break

                elif _sum + seq_list[i] < c:
                    tmp_lst.append(seq_list[i])
                    _sum += seq_list[i]

                # _sum + seq_list[i] < c
                else:
                    tmp_lst = []
                    _sum = 0
                    break

    biggest = (0, None)
    for seq in all_lst:
        if len(seq) > biggest[0]:
            biggest = (len(seq), seq)
    return biggest[1]


class TestStringMethods(unittest.TestCase):
    def test_biggest_seq(self):
        seq = [[5, 2, 6, 4, 1, 1, 1, 3, 3, 1],
               [1, 1, 1, 1, 1, 3, 3, 1, 4],
               [4],
               [-1, -2, -3, 1, 2, 0, 4]]
        c = (7, 4, 4, 5)

        self.assertEqual(biggest_seq(seq[0], c[0]), [4, 1, 1, 1])
        self.assertEqual(biggest_seq(seq[1], c[1]), [1, 1, 1, 1])
        self.assertEqual(biggest_seq(seq[2], c[2]), [4])
        self.assertEqual(biggest_seq(seq[3], c[3]), None)


if __name__ == '__main__':
    unittest.main()
