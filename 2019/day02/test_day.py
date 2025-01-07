import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "1,9,10,3,2,3,11,0,99,30,40,50",
        ]

        self.assertEqual(3500, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))
