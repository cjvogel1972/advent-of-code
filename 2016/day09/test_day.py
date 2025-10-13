import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))

    def test_decompress_version_1(self):
        self.assertEqual("ADVENT", day.decompress("ADVENT", 1))
        self.assertEqual("ABBBBBC", day.decompress("A(1x5)BC", 1))
        self.assertEqual("XYZXYZXYZ", day.decompress("(3x3)XYZ", 1))
        self.assertEqual("ABCBCDEFEFG", day.decompress("A(2x2)BCD(2x2)EFG", 1))
        self.assertEqual("(1x3)A", day.decompress("(6x1)(1x3)A", 1))
        self.assertEqual("X(3x3)ABC(3x3)ABCY", day.decompress("X(8x2)(3x3)ABCY", 1))

    def test_decompress_version_2(self):
        self.assertEqual("XYZXYZXYZ", day.decompress("(3x3)XYZ", 2))
        self.assertEqual("XABCABCABCABCABCABCY", day.decompress("X(8x2)(3x3)ABCY", 2))
        self.assertEqual(241920, len(day.decompress("(27x12)(20x12)(13x14)(7x10)(1x12)A", 2)))
        self.assertEqual(445, len(day.decompress("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 2)))
