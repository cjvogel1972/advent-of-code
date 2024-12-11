import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        directions = {
            "R2, L3": 5,
            "R2, R2, R2": 2,
            "R5, L5, R5, R3": 12
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "R8, R4, R4, R8"
        ]

        self.assertEqual(4, day.solve_part2(lines))
