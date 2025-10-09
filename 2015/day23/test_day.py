import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "inc a",
            "jio a, +2",
            "tpl a",
            "inc a",
        ]

        self.assertEqual(2, day.run_program(lines, 0, 0)[0])

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))
