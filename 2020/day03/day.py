from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    grid = [[c for c in line] for line in lines]
    slope = (1, 3)

    return count_trees(slope, grid)


def solve_part2(lines: list[str]) -> int:
    grid = [[c for c in line] for line in lines]
    slopes = [(1,1), (1, 3), (1,5), (1,7), (2,1)]

    result = 1
    for slope in slopes:
        result *= count_trees(slope, grid)

    return result


def count_trees(slope: tuple[int, int], grid: list[list[str]]) -> int:
    loc = (0, 0)
    trees = 0

    while loc[0] < len(grid):
        y, x = loc
        x = x % len(grid[0])
        if grid[y][x] == "#":
            trees += 1
        loc = tuple_add(loc, slope)

    return trees
