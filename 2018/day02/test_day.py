import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"
        ]

        self.assertEqual(12, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"
        ]

        self.assertEqual("fgij", day.solve_part2(lines))
