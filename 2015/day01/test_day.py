import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        directions = {
            "(())": 0,
            "()()": 0,
            "(((": 3,
            "(()(()(": 3,
            "))(((((": 3,
            "())": -1,
            "))(": -1,
            ")))": -3,
            ")())())": -3
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part1(lines))

    def test_solve_part2(self):
        directions = {
            ")": 1,
            "()())": 5
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part2(lines))
