import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "123 -> x",
            "456 -> y",
            "x AND y -> d",
            "x OR y -> e",
            "x LSHIFT 2 -> f",
            "y RSHIFT 2 -> g",
            "NOT x -> h",
            "NOT y -> i",
        ]
        gates, wires = day.parse_input(lines)

        day.solve_circuit(gates, wires)

        self.assertEqual(72, wires['d'])
        self.assertEqual(507, wires['e'])
        self.assertEqual(492, wires['f'])
        self.assertEqual(114, wires['g'])
        self.assertEqual(65412, wires['h'])
        self.assertEqual(65079, wires['i'])
        self.assertEqual(123, wires['x'])
        self.assertEqual(456, wires['y'])

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))
