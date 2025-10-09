import unittest

import day


class Test(unittest.TestCase):

    def test_play_turns_first_example(self):
        boss = day.Boss(13, 8)
        wizard = day.Wizard(10, 250)

        winner = day.play_turns(wizard, boss)
        self.assertIsNotNone(winner)
        self.assertEqual(226, winner.mana_spent)

    def test_play_turns_second_example(self):
        boss = day.Boss(14, 8)
        wizard = day.Wizard(10, 250)

        winner = day.play_turns(wizard, boss)
        self.assertIsNotNone(winner)
        self.assertEqual(641, winner.mana_spent)

    def test_last_turn(self):
        boss = day.Boss(10, 8)
        wizard = day.Wizard(2, 77)
        wizard.active_spells.append(day.SpellTimer('Poison', 5))

        winner, keep_playing = day.player_turn(wizard, boss)
        self.assertEqual(0, len(keep_playing))
        self.assertIsNotNone(winner)
        self.assertEqual(53, winner.mana_spent)

    def test_lose_hit_points_with_shield_greater_than_damage(self):
        player = day.Wizard(10, 10)
        player.armor = 7
        player.lose_hit_points(6)

        self.assertEqual(player.hit_points, 9)

    def test_boss_turn_with_active_spell_that_will_kill(self):
        boss = day.Boss(3, 8)
        wizard = day.Wizard(2, 24)
        wizard.active_spells.append(day.SpellTimer('Poison', 2))

        day.boss_turn(wizard, boss)

        self.assertFalse(boss.is_alive())
        self.assertEqual(wizard.hit_points, 2)

    def test_apply_active_spells_with_spell_expiring(self):
        boss = day.Boss(3, 8)
        wizard = day.Wizard(10, 250)
        wizard.active_spells.append(day.SpellTimer('Recharge', 1))
        wizard.active_spells.append(day.SpellTimer('Shield', 4))

        wizard.apply_active_spells(boss)

        self.assertEqual(1, len(wizard.active_spells))
        self.assertEqual('Shield', wizard.active_spells[0].name)