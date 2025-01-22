import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        passwords = {
            "abcdefgh": "abcdffaa",
            "ghijklmn": "ghjaabcc"
        }

        for password in passwords:
            lines = [password]
            self.assertEqual(passwords[password], day.solve_part1(lines))

    def test_increment_password(self):
        self.assertEqual("abcdefgi", day.increment_password("abcdefgh"))
        self.assertEqual("abcdefha", day.increment_password("abcdefgz"))

    def test_is_good_password(self):
        passwords = {
            "hijklmmn": False,
            "abbceffg": False,
            "abbcegjk": False,
            "abcdffaa": True,
            "ghjaabcc": True
        }

        for password in passwords:
            self.assertEqual(passwords[password], day.is_good_password(password), password)

    def test_has_increasing_letters(self):
        passwords = {
            "hijklmmn": True,
            "abbceffg": False,
            "abbcegjk": False,
            "abcdffaa": True,
            "ghjaabcc": True
        }

        for password in passwords:
            self.assertEqual(passwords[password], day.has_increasing_letters(password), password)

    def test_has_good_letters(self):
        passwords = {
            "hijklmmn": False,
            "abbceffg": True,
            "abbcegjk": True,
            "abcdffaa": True,
            "ghjaabcc": True
        }

        for password in passwords:
            self.assertEqual(passwords[password], day.has_good_letters(password), password)

    def test_has_two_non_overlapping(self):
        passwords = {
            "hijklmmn": False,
            "abbceffg": True,
            "abbcegjk": False,
            "abcdffaa": True,
            "ghjaabcc": True
        }

        for password in passwords:
            self.assertEqual(passwords[password], day.has_two_non_overlapping(password), password)
