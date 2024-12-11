import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        directions = {
            "1122": 3,
            "1111": 4,
            "1234": 0,
            "91212129": 9,
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part1(lines))

    def test_solve_part2(self):
        directions = {
            "1212": 6,
            "1221": 0,
            "123425": 4,
            "123123": 12,
            "12131415": 4,
        }
        for line in directions:
            lines = [
                line
            ]

            self.assertEqual(directions[line], day.solve_part2(lines))
