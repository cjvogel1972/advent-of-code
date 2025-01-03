import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "ULL",
            "RRDDD",
            "LURDL",
            "UUUUD"
        ]

        self.assertEqual(1985, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "ULL",
            "RRDDD",
            "LURDL",
            "UUUUD"
        ]

        self.assertEqual("5DB3", day.solve_part2(lines))
