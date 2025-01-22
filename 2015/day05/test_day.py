import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "ugknbfddgicrmopn",
            "aaa",
            "jchzalrnumimnmhp",
            "haegwjzuvuyypxyu",
            "dvszwmarrgswjxmb"
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "qjhvhtzxzqqjkmpb",
            "xxyxx",
            "uurcxstgmygtbstg",
            "ieodomkazucvgmuy"
        ]

        self.assertEqual(2, day.solve_part2(lines))
