import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "abcdef",
        ]

        self.assertEqual(609043, day.solve_part1(lines))

    def test_solve_part1_example2(self):
        lines = [
            "pqrstuv",
        ]

        self.assertEqual(1048970, day.solve_part1(lines))
