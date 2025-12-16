import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "7,1",
            "11,1",
            "11,7",
            "9,7",
            "9,5",
            "2,5",
            "2,3",
            "7,3",
        ]

        self.assertEqual(50, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "7,1",
            "11,1",
            "11,7",
            "9,7",
            "9,5",
            "2,5",
            "2,3",
            "7,3",
        ]

        self.assertEqual(24, day.solve_part2(lines))
