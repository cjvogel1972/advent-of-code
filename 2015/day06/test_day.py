import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "turn on 0,0 through 999,999",
        ]

        self.assertEqual(1000000, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "turn on 0,0 through 0,0",
            "toggle 0,0 through 999,999",
        ]

        self.assertEqual(2000001, day.solve_part2(lines))
