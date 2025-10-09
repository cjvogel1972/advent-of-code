from copy import deepcopy
from collections import deque


class Boss:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    def lose_hit_points(self, damage):
        self.hit_points -= damage

    def is_alive(self) -> bool:
        return self.hit_points > 0

    def copy(self):
        return Boss(self.hit_points, self.damage)


class Wizard:
    def __init__(self, hit_points, mana):
        self.hit_points = hit_points
        self.mana = mana
        self.active_spells = []
        self.armor = 0
        self.mana_spent = 0

    def lose_hit_points(self, damage):
        computed_damage = damage - self.armor
        if computed_damage <= 0:
            computed_damage = 1

        self.hit_points -= computed_damage

    def copy(self):
        dup = Wizard(self.hit_points, self.mana)
        dup.active_spells = deepcopy(self.active_spells)
        dup.armor = self.armor
        dup.mana_spent = self.mana_spent
        return dup

    def is_alive(self) -> bool:
        return self.hit_points > 0

    def can_cast_spell(self, spell) -> bool:
        spell_active = any(s.name == spell.name for s in self.active_spells)
        return spell.cost <= self.mana and not spell_active

    def cast_spell(self, spell, boss: Boss):
        self.mana -= spell.cost
        self.mana_spent += spell.cost
        if spell.duration > 0:
            self.active_spells.append(SpellTimer(spell.name, spell.duration))
        else:
            spell.apply(self, boss)

    def apply_active_spells(self, boss: Boss):
        for active_spell in self.active_spells:
            spell = spells[active_spell.name]
            spell.apply(self, boss)
            active_spell.decrement_timer()

            if active_spell.duration == 0 and active_spell.name == 'Shield':
                self.armor = 0

        self.active_spells = [s for s in self.active_spells if s.duration > 0]


class Spell:
    def __init__(self, name: str, cost: int, damage: int, armor: int, heals: int, new_mana: int, duration: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.heals = heals
        self.new_mana = new_mana
        self.duration = duration

    def apply(self, wizard: Wizard, boss: Boss):
        if self.damage > 0:
            boss.lose_hit_points(self.damage)
        if self.heals > 0:
            wizard.hit_points += self.heals
        if self.new_mana > 0:
            wizard.mana += self.new_mana
        if self.armor > 0:
            wizard.armor = self.armor


class SpellTimer:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def decrement_timer(self):
        self.duration -= 1


spells = {
    'Magic Missile': Spell('Magic Missile', 53, 4, 0, 0, 0, 0),
    'Drain': Spell('Drain', 73, 2, 0, 2, 0, 0),
    'Shield': Spell('Shield', 113, 0, 7, 0, 0, 6),
    'Poison': Spell('Poison', 173, 3, 0, 0, 0, 6),
    'Recharge': Spell('Recharge', 229, 0, 0, 0, 101, 5),
}


def solve_part1(lines: list[str]) -> int:
    boss = Boss(*parse_boss_input(lines))
    player = Wizard(50, 500)

    winner = play_turns(player, boss)
    return winner.mana_spent


def solve_part2(lines: list[str]) -> int:
    boss = Boss(*parse_boss_input(lines))
    player = Wizard(50, 500)

    winner = play_turns(player, boss, True)
    return winner.mana_spent


def parse_boss_input(lines: list[str]) -> tuple[int, int]:
    hit_points = int(lines[0].split(": ")[1])
    damage = int(lines[1].split(": ")[1])

    return hit_points, damage


def play_turns(player: Wizard, boss: Boss, hard: bool = False):
    winner = None
    states = deque([(player, boss)])

    while states:
        p, b = states.pop()
        if winner is not None and winner.mana_spent < p.mana_spent:
            continue

        round_winner, new_states = player_turn(p, b, hard)
        if round_winner is not None:
            winner = update_winner(winner, round_winner)

        states.extend(new_states)

    return winner


def player_turn(player: Wizard, boss: Boss, hard: bool = False):
    winner = None
    new_states = []

    if hard:
        player.hit_points -= 1
        if not player.is_alive():
            return winner, new_states

    player.apply_active_spells(boss)

    if not boss.is_alive():
        return player, new_states

    for spell in spells.values():
        if player.can_cast_spell(spell):
            p2 = player.copy()
            b2 = boss.copy()
            p2.cast_spell(spell, b2)

            if b2.is_alive():
                boss_turn(p2, b2)
                if b2.is_alive() and p2.is_alive():
                    new_states.append((p2, b2))
                elif p2.is_alive():
                    winner = update_winner(winner, p2)
            else:
                winner = update_winner(winner, p2)

    if winner is not None:
        new_states = [state for state in new_states if state[0].mana_spent <= winner.mana_spent]

    return winner, new_states


def boss_turn(player: Wizard, boss: Boss):
    player.apply_active_spells(boss)

    if boss.is_alive():
        player.lose_hit_points(boss.damage)


def update_winner(current_winner, candidate):
    if current_winner is None or candidate.mana_spent < current_winner.mana_spent:
        return candidate
    return current_winner
