import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "0:",
            "###",
            "##.",
            "##.",
            "",
            "1:",
            "###",
            "##.",
            ".##",
            "",
            "2:",
            ".##",
            "###",
            "##.",
            "",
            "3:",
            "##.",
            "###",
            "##",
            "",
            "4:",
            "###",
            "#..",
            "###",
            "",
            "5:",
            "###",
            ".#.",
            "###",
            "",
            "4x4: 0 0 0 0 2 0",
            "12x5: 1 0 1 0 2 2",
            "12x5: 1 0 1 0 3 2",
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))
