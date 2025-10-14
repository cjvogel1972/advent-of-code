import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "value 5 goes to bot 2",
            "bot 2 gives low to bot 1 and high to bot 0",
            "value 3 goes to bot 1",
            "bot 1 gives low to output 1 and high to bot 0",
            "bot 0 gives low to output 2 and high to output 0",
            "value 2 goes to bot 2",
        ]

        self.assertEqual(2, day.find_bot_with_chips(lines, [2, 5]))
