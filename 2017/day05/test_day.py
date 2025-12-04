import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "0",
            "3",
            "0",
            "1",
            "-3",
        ]

        self.assertEqual(5, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "0",
            "3",
            "0",
            "1",
            "-3",
        ]

        self.assertEqual(10, day.solve_part2(lines))
