import unittest

import day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "Hit Points: 100",
            "Damage: 8",
            "Armor: 2",
        ]

        self.assertEqual(0, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "",
        ]

        self.assertEqual(0, day.solve_part2(lines))

    def test_compute_new_hit_points(self):
        self.assertEqual(3, day.compute_damage_to(2, 5))
        self.assertEqual(1, day.compute_damage_to(300, 5))

    def test_player_wins(self):
        self.assertTrue(day.player_wins(12, 7, 2, 8, 5, 5))
        self.assertFalse(day.player_wins(100, 8, 2, 100, 9, 0))
