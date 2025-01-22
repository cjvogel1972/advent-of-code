import itertools
import re

PARSER = re.compile("(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)")


def solve_part1(lines: list[str]) -> int:
    names, rules = parse_input(lines)

    return compute_max_happiness(names, rules)


def solve_part2(lines: list[str]) -> int:
    names, rules = parse_input(lines)

    for name in names:
        rules[("Me", name)] = 0
        rules[(name, "Me")] = 0

    names.add("Me")

    return compute_max_happiness(names, rules)


def parse_input(lines):
    names = set()
    rules = {}

    for line in lines:
        name1, gain_loss, value, name2 = PARSER.match(line).groups()
        names.add(name1)
        names.add(name2)
        rules[(name1, name2)] = int(value) * (1 if gain_loss == "gain" else -1)

    return names, rules


def compute_max_happiness(names, rules):
    max_happiness = 0
    arrangements = list(itertools.permutations(names))

    for arrangement in arrangements:
        happiness = rules[(arrangement[0], arrangement[-1])] + rules[(arrangement[-1], arrangement[0])]
        for a, b in zip(arrangement, arrangement[1:]):
            happiness += rules[(a, b)] + rules[(b, a)]
        max_happiness = max(max_happiness, happiness)

    return max_happiness
