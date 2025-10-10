import unittest

import day


class Test(unittest.TestCase):

    def test_balance_packages_example_1(self):
        lines = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "7",
            "8",
            "9",
            "10",
            "11"
        ]

        self.assertEqual(99, day.balance_packages(lines, 3))

    def test_find_package_combination_of_weights_equal_to_sum(self):
        packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
        packages.sort(reverse=True)
        sum = 20

        self.assertEqual(25, len(day.find_package_combinations_equal_to_expected_weight(sum, packages)))

    def test_balance_packages_example_2(self):
        lines = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "7",
            "8",
            "9",
            "10",
            "11"
        ]

        self.assertEqual(44, day.balance_packages(lines, 4))