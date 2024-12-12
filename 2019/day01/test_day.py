import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        mass = {
            "12": 2,
            "14": 2,
            "1969": 654,
            "100756": 33583
        }
        for line in mass:
            lines = [
                line
            ]

            self.assertEqual(mass[line], day.solve_part1(lines))

    def test_solve_part2(self):
        mass = {
            "14": 2,
            "1969": 966,
            "100756": 50346
        }
        for line in mass:
            lines = line.strip().split("\n")

            self.assertEqual(mass[line], day.solve_part2(lines))
