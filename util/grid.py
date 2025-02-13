from typing import Any

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

cardinal_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def manhattan_distance(loc1: tuple[int, int], loc2: tuple[int, int]) -> int:
    """Compute the Manhattan distance between two coordinates"""
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def good_square(grid: list[list[Any]], r: int, c: int) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[r])


def good_square_tuple(grid: list[list[Any]], pos: tuple[int, int]) -> bool:
    return good_square(grid, pos[0], pos[1])


def print_grid(grid: list[list[Any]]):
    print("\n".join("".join(str(row)) for row in grid))
