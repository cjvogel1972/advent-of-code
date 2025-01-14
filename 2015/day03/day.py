from util.grid import cardinal_directions
from util.tuple import tuple_add

DIRECTION_MAPPING = {'^': 0, '>': 1, 'v': 2, '<': 3}


def solve_part1(lines: list[str]) -> int:
    loc = (0, 0)
    houses = {loc}

    for direction in lines[0]:
        loc = move(loc, direction, houses)

    return len(houses)


def solve_part2(lines: list[str]) -> int:
    santa_loc = robo_loc = (0, 0)
    houses = {santa_loc, robo_loc}

    for i, direction in enumerate(lines[0]):
        if i % 2 == 0:
            santa_loc = move(santa_loc, direction, houses)
        else:
            robo_loc = move(robo_loc, direction, houses)

    return len(houses)


def move(loc: tuple[int, int], direction: str, houses: set[tuple[int, int]]) -> tuple[int, int]:
    loc = tuple_add(loc, cardinal_directions[DIRECTION_MAPPING[direction]])
    houses.add(loc)

    return loc
