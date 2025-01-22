import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = """""
"abc"
"aaa\\"aaa"
"\\x27"
""".splitlines()

        self.assertEqual(12, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = """""
"abc"
"aaa\\"aaa"
"\\x27"
""".splitlines()

        self.assertEqual(19, day.solve_part2(lines))
