import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "3, 4, 1, 5",
        ]

        sparse_hash = day.create_sparse_hash(5, lines[0])
        self.assertEqual(12, sparse_hash[0] * sparse_hash[1])

    def test_solve_part2(self):
        self.assertEqual("a2582a3a0e66e6e86e3812dcb672a272", day.solve_part2([""]))
        self.assertEqual("33efeb34ea91902bb2f59c9920caa6cd", day.solve_part2(["AoC 2017"]))
        self.assertEqual("3efbe78a8d82f29979031a4aa0b16a9d", day.solve_part2(["1,2,3"]))
        self.assertEqual("63960835bcdc130f0b66d7ff4f6a5a8e", day.solve_part2(["1,2,4"]))
