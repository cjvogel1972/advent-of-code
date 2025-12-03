import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]

        self.assertEqual(357, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]

        self.assertEqual(3121910778619, day.solve_part2(lines))
