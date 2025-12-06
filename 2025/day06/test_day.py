import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]

        self.assertEqual(4277556, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   +  ",
        ]

        self.assertEqual(3263827, day.solve_part2(lines))
