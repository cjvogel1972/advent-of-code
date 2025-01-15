import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            " 5 10 25",
        ]

        self.assertEqual(0, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "101 301 501",
            "102 302 502",
            "103 303 503",
            "201 401 601",
            "202 402 602",
            "203 403 603",
        ]

        self.assertEqual(6, day.solve_part2(lines))
