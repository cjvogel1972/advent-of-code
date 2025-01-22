import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83",
        ]

        self.assertEqual(159, day.solve_part1(lines))

    def test_solve_part1_simple(self):
        lines = [
            "R8,U5,L5,D3",
            "U7,R6,D4,L4",
        ]

        self.assertEqual(6, day.solve_part1(lines))

    def test_solve_part1_example_2(self):
        lines = [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        ]

        self.assertEqual(135, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83",
        ]

        self.assertEqual(610, day.solve_part2(lines))

    def test_solve_part2_simple(self):
        lines = [
            "R8,U5,L5,D3",
            "U7,R6,D4,L4",
        ]

        self.assertEqual(30, day.solve_part2(lines))

    def test_solve_part2_example_2(self):
        lines = [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
        ]

        self.assertEqual(410, day.solve_part2(lines))
