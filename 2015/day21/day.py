from collections import namedtuple

Item = namedtuple('Item', ['cost', 'damage', 'armor'])
Combatant = namedtuple('Combatant', ['hit_points', 'damage', 'armor'])

WEAPONS = [Item(8, 4, 0), Item(10, 5, 0), Item(25, 6, 0), Item(40, 7, 0), Item(74, 8, 0)]
ARMOR = [Item(0, 0, 0), Item(13, 1, 0), Item(31, 2, 0), Item(53, 3, 0), Item(75, 4, 0), Item(102, 5, 0)]
RINGS = [Item(0, 0, 0), Item(25, 1, 0), Item(50, 2, 0), Item(100, 3, 0), Item(20, 0, 1), Item(40, 0, 2), Item(80, 0, 3)]


def solve_part1(lines: list[str]) -> int:
    boss = parse_boss_input(lines)
    player = Combatant(100, 0, 0)

    least_gold_spent = float('inf')

    for weapon in WEAPONS:
        for armor in ARMOR:
            for ring1 in RINGS:
                for ring2 in RINGS:
                    if ring1 == ring2 and ring1[0] != 0:
                        continue

                    items = [weapon, armor, ring1, ring2]
                    if win_with_items(boss, player, items):
                        cost = sum(item.cost for item in items)
                        least_gold_spent = min(least_gold_spent, cost)

    return least_gold_spent


def solve_part2(lines: list[str]) -> int:
    boss = parse_boss_input(lines)
    player = Combatant(100, 0, 0)

    max_gold_spent = 0

    for weapon in WEAPONS:
        for armor in ARMOR:
            for ring1 in RINGS:
                for ring2 in RINGS:
                    if ring1 == ring2 and ring1[0] != 0:
                        continue

                    items = [weapon, armor, ring1, ring2]
                    if not win_with_items(boss, player, items):
                        cost = sum(item.cost for item in items)
                        max_gold_spent = max(max_gold_spent, cost)

    return max_gold_spent


def parse_boss_input(lines) -> Combatant:
    hit_points = int(lines[0].split(": ")[1])
    damage = int(lines[1].split(": ")[1])
    armor = int(lines[2].split(": ")[1])

    return Combatant(hit_points, damage, armor)


def win_with_items(boss: Combatant, player: Combatant, items: list[Item]) -> bool:
    player_damage = sum(item.damage for item in items)
    player_armor = sum(item.armor for item in items)
    player = Combatant(player.hit_points, player_damage, player_armor)

    return player_wins(boss, player)


def player_wins(boss: Combatant, player: Combatant) -> bool:
    damage_to_boss = compute_damage_to(boss.armor, player.damage)
    damage_to_player = compute_damage_to(player.armor, boss.damage)

    hits_to_boss = (boss.hit_points // damage_to_boss) + (1 if boss.hit_points % damage_to_boss else 0)
    hits_to_player = (player.hit_points // damage_to_player) + (1 if player.hit_points % damage_to_player else 0)

    return hits_to_boss <= hits_to_player


def compute_damage_to(armor: int, damage: int) -> int:
    d = damage - armor

    return d if d > 0 else 1
