import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "abc",
        ]

        self.assertEqual("18f47a30", day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "abc",
        ]

        self.assertEqual("05ace8e3", day.solve_part2(lines))
