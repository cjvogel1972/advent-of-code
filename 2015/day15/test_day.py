import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]

        self.assertEqual(62842880, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
        ]

        self.assertEqual(57600000, day.solve_part2(lines))
