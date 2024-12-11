from util.grid import cardinal_directions, manhattan_distance
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    directions = lines[0].strip().split(", ")
    direction_index = 0

    location = (0, 0)
    for direction in directions:
        turn = direction[0]
        blocks = int(direction[1:])
        if turn == "R":
            direction_index = 0 if direction_index + 1 > 3 else direction_index + 1
        else:
            direction_index = 3 if direction_index - 1 < 0 else direction_index - 1
        location = tuple_add(location, (
            cardinal_directions[direction_index][0] * blocks, cardinal_directions[direction_index][1] * blocks))

    return manhattan_distance((0, 0), location)


def solve_part2(lines: list[str]) -> int:
    directions = lines[0].strip().split(", ")
    direction_index = 0

    location = (0, 0)
    visited = set(location)
    for direction in directions:
        turn = direction[0]
        blocks = int(direction[1:])
        if turn == "R":
            direction_index = 0 if direction_index + 1 > 3 else direction_index + 1
        else:
            direction_index = 3 if direction_index - 1 < 0 else direction_index - 1
        for _ in range(blocks):
            location = tuple_add(location, cardinal_directions[direction_index])
            if location in visited:
                break
            visited.add(location)
        else:
            continue
        break

    return manhattan_distance((0, 0), location)
