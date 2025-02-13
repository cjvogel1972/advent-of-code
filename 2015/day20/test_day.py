import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "60",
        ]

        self.assertEqual(4, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))

    def test_presents_per_house_infinite_visits(self):
        self.assertEqual(10, day.presents_for_house_infinite_visits(1))
        self.assertEqual(30, day.presents_for_house_infinite_visits(2))
        self.assertEqual(40, day.presents_for_house_infinite_visits(3))
        self.assertEqual(70, day.presents_for_house_infinite_visits(4))
        self.assertEqual(60, day.presents_for_house_infinite_visits(5))
        self.assertEqual(120, day.presents_for_house_infinite_visits(6))
        self.assertEqual(80, day.presents_for_house_infinite_visits(7))
        self.assertEqual(150, day.presents_for_house_infinite_visits(8))
        self.assertEqual(130, day.presents_for_house_infinite_visits(9))

    def test_presents_per_house_fifty_visits(self):
        self.assertEqual(1023, day.presents_for_house_fifty_visits(50))
        self.assertEqual(781, day.presents_for_house_fifty_visits(51))
        self.assertEqual(2376, day.presents_for_house_fifty_visits(100))
        self.assertEqual(1111, day.presents_for_house_fifty_visits(101))
        self.assertEqual(2343, day.presents_for_house_fifty_visits(102))
