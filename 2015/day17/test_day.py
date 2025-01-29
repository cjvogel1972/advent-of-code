import unittest

import day


class Test(unittest.TestCase):

    def test_fill_containers(self):
        containers = [20, 15, 10, 5, 5]
        result = day.fill_containers(containers, 25)

        self.assertEqual(4, len(result))

    def test_solve_part2(self):
        containers = [20, 15, 10, 5, 5]
        result = day.fill_containers(containers, 25)

        self.assertEqual(3, day.count_minimum_containers(result))
