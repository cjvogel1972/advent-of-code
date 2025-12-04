import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "0 2 7 0",
        ]

        self.assertEqual(5, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "0 2 7 0",
        ]

        self.assertEqual(4, day.solve_part2(lines))
