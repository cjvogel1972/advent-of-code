import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]

        self.assertEqual(3, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]

        self.assertEqual(6, day.solve_part2(lines))

    def test_solve_part2_huge_rotation_forward(self):
        lines = [
            "R1000",
        ]

        self.assertEqual(10, day.solve_part2(lines))

    def test_solve_part2_huge_rotation_forward_land_on_0(self):
        lines = [
            "R1050",
        ]

        self.assertEqual(11, day.solve_part2(lines))

    def test_solve_part2_huge_rotation_backward(self):
        lines = [
            "L1000",
        ]

        self.assertEqual(10, day.solve_part2(lines))

    def test_solve_part2_huge_rotation_backward_land_on_0(self):
        lines = [
            "L1050",
        ]

        self.assertEqual(11, day.solve_part2(lines))
