import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "5 1 9 5",
            "7 5 3",
            "2 4 6 8",
        ]

        self.assertEqual(18, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "5 9 2 8",
            "9 4 7 3",
            "3 8 6 5",
        ]

        self.assertEqual(9, day.solve_part2(lines))
