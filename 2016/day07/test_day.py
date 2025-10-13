import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "abba[mnop]qrst",
            "abcd[bddb]xyyx",
            "aaaa[qwer]tyui",
            "ioxxoj[asdfgh]zxcvbn"
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "aba[bab]xyz",
            "xyx[xyx]xyx",
            "aaa[kek]eke",
            "zazbz[bzb]cdb"
        ]

        self.assertEqual(3, day.solve_part2(lines))
