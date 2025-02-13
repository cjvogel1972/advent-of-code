import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "H => HO",
            "H => OH",
            "O => HH",
            "",
            "HOH"
        ]

        self.assertEqual(4, day.solve_part1(lines))

    def test_solve_part1_example2(self):
        lines = [
            "H => HO",
            "H => OH",
            "O => HH",
            "",
            "HOHOHO"
        ]

        self.assertEqual(7, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "e => H",
            "e => O",
            "H => HO",
            "H => OH",
            "O => HH",
            "",
            "HOH"
        ]

        self.assertEqual(3, day.solve_part2(lines))

    def test_solve_part2_example2(self):
        lines = [
            "e => H",
            "e => O",
            "H => HO",
            "H => OH",
            "O => HH",
            "",
            "HOHOHO"
        ]

        self.assertEqual(6, day.solve_part2(lines))
