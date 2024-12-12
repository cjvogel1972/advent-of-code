import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "1721",
            "979",
            "366",
            "299",
            "675",
            "1456"
        ]

        self.assertEqual(514579, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "1721",
            "979",
            "366",
            "299",
            "675",
            "1456"
        ]

        self.assertEqual(241861950, day.solve_part2(lines))
