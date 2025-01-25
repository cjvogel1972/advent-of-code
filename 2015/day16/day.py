import re

PARSER = re.compile(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")
ANALYSIS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def solve_part1(lines: list[str]) -> int:
    for line in lines:
        info = PARSER.match(line).groups()
        if ANALYSIS[info[1]] == int(info[2]) and ANALYSIS[info[3]] == int(info[4]) and ANALYSIS[info[5]] == int(
                info[6]):
            return int(info[0])

    return 0


def solve_part2(lines: list[str]) -> int:
    for line in lines:
        info = PARSER.match(line).groups()
        if check_info(info[1], int(info[2])) and check_info(info[3], int(info[4])) and check_info(info[5], int(info[6])):
            return int(info[0])

    return 0


def check_info(name: str, value: int) -> bool:
    if name in ['cats', 'trees']:
        return value > ANALYSIS[name]

    if name in ['pomeranians', 'goldfish']:
        return value < ANALYSIS[name]

    return value == ANALYSIS[name]
