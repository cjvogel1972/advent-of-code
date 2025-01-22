import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ]

        self.assertEqual(605, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "London to Dublin = 464",
            "London to Belfast = 518",
            "Dublin to Belfast = 141",
        ]

        self.assertEqual(982, day.solve_part2(lines))
