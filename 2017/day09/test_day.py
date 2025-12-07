import unittest

import day


class Test(unittest.TestCase):

    def test_score_groups(self):
        self.assertEqual(1, day.score_groups("{}"))
        self.assertEqual(6, day.score_groups("{{{}}}"))
        self.assertEqual(5, day.score_groups("{{},{}}"))
        self.assertEqual(16, day.score_groups("{{{},{},{{}}}}"))
        self.assertEqual(1, day.score_groups("{<{},{},{{}}>}"))
        self.assertEqual(9, day.score_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
        self.assertEqual(9, day.score_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
        self.assertEqual(3, day.score_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}"))

    def test_count_garbage(self):
        self.assertEqual(0, day.count_garbage("<>"))
        self.assertEqual(17, day.count_garbage("<random characters>"))
        self.assertEqual(3, day.count_garbage("<<<<>"))
        self.assertEqual(2, day.count_garbage("<{!>}>"))
        self.assertEqual(0, day.count_garbage("<!!>"))
        self.assertEqual(0, day.count_garbage("<!!!>>"))
        self.assertEqual(10, day.count_garbage("<{o\"i!a,<{i<a>"))
