import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            ".#.#.#",
            "...##.",
            "#....#",
            "..#...",
            "#.#..#",
            "####..",
        ]
        lights = [[l for l in line] for line in lines]

        self.assertEqual(4, day.count_lights_on(day.animate(lights, 4, False)))

    def test_solve_part2(self):
        lines = [
            ".#.#.#",
            "...##.",
            "#....#",
            "..#...",
            "#.#..#",
            "####..",
        ]
        lights = [[l for l in line] for line in lines]
        lights[0][0] = lights[0][5] = lights[5][0] = lights[5][5] = '#'

        self.assertEqual(17, day.count_lights_on(day.animate(lights, 5, True)))
