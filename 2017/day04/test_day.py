import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "aa bb cc dd ee",
            "aa bb cc dd aa",
            "aa bb cc dd aaa",
        ]

        self.assertEqual(2, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))

    def test_valid_passphrase(self):
        self.assertTrue(day.valid_passphrase("aa bb cc dd ee"))
        self.assertFalse(day.valid_passphrase("aa bb cc dd aa"))
        self.assertTrue(day.valid_passphrase("aa bb cc dd aaa"))

    def test_valid_passphrase_no_anagrams(self):
        self.assertTrue(day.valid_passphrase_no_anagrams("abcde fghij"))
        self.assertFalse(day.valid_passphrase_no_anagrams("abcde xyz ecdab"))
        self.assertTrue(day.valid_passphrase_no_anagrams("a ab abc abd abf abj"))
        self.assertTrue(day.valid_passphrase_no_anagrams("iiii oiii ooii oooi oooo"))
        self.assertFalse(day.valid_passphrase_no_anagrams("oiii ioii iioi iiio"))
