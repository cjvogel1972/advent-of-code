import unittest

import day


class Test(unittest.TestCase):

    def test_compute_distance(self):
        self.assertEqual(1120, day.compute_distance(14, 10, 127, 1000))
        self.assertEqual(1056, day.compute_distance(16, 11, 162, 1000))

    def test_compute_max_score(self):
        reindeer = {'Comet': day.Reindeer('Comet', 14, 10, 127),
                    'Dancer': day.Reindeer('Dancer', 16, 11, 162)}

        self.assertEqual(689, day.compute_max_score(reindeer, 1000))
