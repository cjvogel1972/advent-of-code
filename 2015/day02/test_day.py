import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "2x3x4",
            "1x1x10"
        ]

        self.assertEqual(101, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "2x3x4",
            "1x1x10"
        ]

        self.assertEqual(48, day.solve_part2(lines))
