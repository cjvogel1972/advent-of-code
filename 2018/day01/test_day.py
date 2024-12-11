import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        directions = {
            "+1\n-2\n+3\n+1\n": 3,
            "+1\n+1\n+1\n": 3,
            "+1\n+1\n-2\n": 0,
            "-1\n-2\n-3\n": -6
        }
        for line in directions:
            lines = line.strip().split("\n")

            self.assertEqual(directions[line], day.solve_part1(lines))

    def test_solve_part2(self):
        directions = {
            "+1\n-2\n+3\n+1\n": 2,
            "+1\n-1\n": 0,
            "+3\n+3\n+4\n-2\n-4\n": 10,
            "-6\n+3\n+8\n+5\n-6\n": 5,
            "+7\n+7\n-2\n-7\n-4\n": 14
        }
        for line in directions:
            lines = line.strip().split("\n")

            self.assertEqual(directions[line], day.solve_part2(lines))
