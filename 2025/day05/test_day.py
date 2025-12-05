import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32",
        ]

        self.assertEqual(3, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "3-5",
            "10-14",
            "16-20",
            "12-18",
            "",
            "1",
            "5",
            "8",
            "11",
            "17",
            "32",
        ]

        self.assertEqual(14, day.solve_part2(lines))
