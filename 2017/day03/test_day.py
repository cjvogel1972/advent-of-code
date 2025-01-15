import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        squares = {
            "1": 0,
            "9": 2,
            "12": 3,
            "23": 2,
            "1024": 31,
        }
        for line in squares:
            lines = [
                line
            ]

            self.assertEqual(squares[line], day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "750",
        ]

        self.assertEqual(806, day.solve_part2(lines))
