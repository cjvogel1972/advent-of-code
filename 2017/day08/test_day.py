import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "b inc 5 if a > 1",
            "a inc 1 if b < 5",
            "c dec -10 if a >= 1",
            "c inc -20 if c == 10",
        ]

        self.assertEqual(1, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "b inc 5 if a > 1",
            "a inc 1 if b < 5",
            "c dec -10 if a >= 1",
            "c inc -20 if c == 10",
        ]

        self.assertEqual(10, day.solve_part2(lines))
