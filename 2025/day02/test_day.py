import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
        ]

        self.assertEqual(1227775554, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
        ]

        self.assertEqual(4174379265, day.solve_part2(lines))

    def test_is_valid_id_part1(self):
        self.assertFalse(day.is_valid_id_part1("11"))
        self.assertFalse(day.is_valid_id_part1("1010"))
        self.assertFalse(day.is_valid_id_part1("446446"))
        self.assertTrue(day.is_valid_id_part1("20"))

    def test_is_valid_id_part2(self):
        self.assertFalse(day.is_valid_id_part2("11"))
        self.assertFalse(day.is_valid_id_part2("111"))
        self.assertFalse(day.is_valid_id_part2("999"))
        self.assertFalse(day.is_valid_id_part2("38593859"))
        self.assertFalse(day.is_valid_id_part2("1188511885"))
        self.assertFalse(day.is_valid_id_part2("2121212121"))