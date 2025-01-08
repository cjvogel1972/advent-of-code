import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc",
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc",
        ]

        self.assertEqual(1, day.solve_part2(lines))
