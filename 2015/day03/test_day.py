import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        directions = {
            ">": 2,
            "^>v<": 4,
            "^v^v^v^v^v": 2,
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part1(lines))

    def test_solve_part2(self):
        directions = {
            "^v": 3,
            "^>v<": 3,
            "^v^v^v^v^v": 11,
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part2(lines))
