import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
        ]

        self.assertEqual(4, day.solve_part1(lines))

    def test_solve_part1_more_overlap(self):
        lines = [
            "#1 @ 0,2: 5x5",
            "#2 @ 3,0: 5x4",
            "#3 @ 4,3: 3x3",
        ]

        self.assertEqual(8, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2",
        ]

        self.assertEqual(3, day.solve_part2(lines))

    def test_overlap(self):
        r1 = day.Rectangle(day.Point(924, 789), day.Point(953, 832))
        r2 = day.Rectangle(day.Point(934, 763), day.Point(949, 822))

        self.assertTrue(day.overlap(r1, r2))
