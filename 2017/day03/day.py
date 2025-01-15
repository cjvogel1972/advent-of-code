from math import sqrt

from util.grid import manhattan_distance, cardinal_directions, directions
from util.tuple import tuple_add

DIR_INDEXES = [0, 3, 2, 1]


def solve_part1(lines: list[str]) -> int:
    num = int(lines[0])
    # the maximum number for a "loop" (square) of the spiral is the bottom right corner. it's square root is 1, 3, 5, 7, etc.
    # we want to find that square root for the inner loop from the given number and then can find the coordinate for
    # the given number (or itself, if the number is that corner number)
    corner_sqrt = int(sqrt(num))
    corner_sqrt -= 1 if corner_sqrt % 2 == 0 else 0
    # this is the length of the side of the "loop" (square) after turning 90 degrees
    side_length = corner_sqrt + 1
    corner_value = corner_sqrt * corner_sqrt
    corner_coord = corner_sqrt // 2
    loc = (corner_coord, corner_coord)

    diff = num - corner_value
    index = 0
    while diff > 0:
        dist = min(diff, side_length)
        if index == 0:
            loc = tuple_add(loc, (0, 1))
            dist -= 1
        loc = tuple_add(loc, tuple(i * dist for i in cardinal_directions[DIR_INDEXES[index]]))
        diff -= side_length
        index += 1

    return manhattan_distance((0, 0), loc)


def solve_part2(lines: list[str]) -> int:
    num = int(lines[0])
    loc = (0, 0)
    last = 1
    squares = {loc: last}

    index = 0
    side_dist = 0
    side_length = 2
    while last < num:
        if index == 0 and side_dist == 0:
            loc = tuple_add(loc, (0, 1))
        else:
            loc = tuple_add(loc, cardinal_directions[DIR_INDEXES[index]])
        last = compute_square_value(squares, loc)
        squares[loc] = last

        side_dist += 1
        if side_dist == side_length:
            side_dist = 0
            index += 1
            if index == 4:
                index = 0
                side_length += 2

    return last


def compute_square_value(squares, loc):
    result = 0
    for d in directions:
        new_loc = tuple_add(loc, d)
        if new_loc in squares:
            result += squares[new_loc]

    return result
