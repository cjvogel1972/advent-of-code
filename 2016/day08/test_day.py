import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "rect 3x2",
            "rotate column x=1 by 1",
            "rotate row y=0 by 4",
            "rotate column x=1 by 1"
        ]
        screen = day.build_screen(7, 3)
        screen = day.run_instructions(lines, screen)

        self.assertEqual(6, day.count_lit_pixels(screen))
