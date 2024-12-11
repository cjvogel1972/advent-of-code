def solve_part1(lines: list[str]) -> int:
    floor = 0

    for c in lines[0]:
        move = 1 if c == '(' else -1
        floor += move

    return floor


def solve_part2(lines: list[str]) -> int:
    floor = 0

    for index, c in enumerate(lines[0]):
        move = 1 if c == '(' else -1
        floor += move
        if floor < 0:
            return index + 1

    return 0
