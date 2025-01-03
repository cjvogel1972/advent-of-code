from util.grid import cardinal_directions, good_square_tuple
from util.tuple import tuple_add

DIRS = {"U": 0, "R": 1, "D": 2, "L": 3}


def solve_part1(lines: list[str]) -> str:
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    curr_loc = (1, 1)

    result = ""
    for line in lines:
        for d in line:
            new_loc = tuple_add(curr_loc, cardinal_directions[DIRS[d]])
            if good_square_tuple(keypad, new_loc):
                curr_loc = new_loc
        result += keypad[curr_loc[0]][curr_loc[1]]

    return result


def solve_part2(lines: list[str]) -> str:
    keypad = [[None, None, "1", None, None],
              [None, "2", "3", "4", None],
              ["5", "6", "7", "8", "9"],
              [None, "A", "B", "C", None],
              [None, None, "D", None, None]]
    curr_loc = (2, 0)

    result = ""
    for line in lines:
        for d in line:
            new_loc = tuple_add(curr_loc, cardinal_directions[DIRS[d]])
            if good_square_tuple(keypad, new_loc) and keypad[new_loc[0]][new_loc[1]] is not None:
                curr_loc = new_loc
        result += keypad[curr_loc[0]][curr_loc[1]]

    return result
