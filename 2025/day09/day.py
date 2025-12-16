from collections import deque
from typing import NamedTuple

from util import grid


def solve_part1(lines: list[str]) -> int:
    coordinates = parse_tile_coordinates(lines)

    areas = [area(corner1, corner2) for i, corner1 in enumerate(coordinates[:-1]) for corner2 in coordinates[i + 1:]]

    return max(areas)


def solve_part2(lines: list[str]) -> int:
    coordinates = parse_tile_coordinates(lines)

    # compress coordinates
    xs = sorted({x for x, _ in coordinates})
    ys = sorted({y for _, y in coordinates})

    tiles = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]

    initialize_polygon_lines(coordinates, tiles, xs, ys)
    flood_fill_green_tiles(tiles)

    psm = construct_prefix_sum_matrix(tiles)

    areas = [area(corner1, corner2) for i, corner1 in enumerate(coordinates[:-1]) for corner2 in coordinates[i + 1:] if
             valid_rectangle(psm, xs, ys, corner1, corner2)]

    return max(areas)


def parse_tile_coordinates(lines: list[str]) -> list[tuple[int, int]]:
    coordinates: list[tuple[int, int]] = []

    for line in lines:
        x, y = map(int, line.split(","))
        coordinates.append((x, y))

    return coordinates


def area(corner1: tuple[int, int], corner2: tuple[int, int]) -> int:
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


def initialize_polygon_lines(coordinates: list[tuple[int, int]], tiles: list[list[int]], xs: list[int], ys: list[int]):
    for (x1, y1), (x2, y2) in zip(coordinates, coordinates[1:] + coordinates[:1]):
        cx1, cx2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])
        cy1, cy2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])
        for cx in range(cx1, cx2 + 1):
            for cy in range(cy1, cy2 + 1):
                tiles[cx][cy] = 1


def flood_fill_green_tiles(tiles: list[list[int]]):
    outside = find_tiles_outside_polygon(tiles)

    for x in range(len(tiles)):
        for y in range(len(tiles[0])):
            if (x, y) not in outside:
                tiles[x][y] = 1


def find_tiles_outside_polygon(tiles: list[list[int]]) -> set[tuple[int, int]]:
    outside = {(-1, -1)}
    queue = deque(outside)

    while queue:
        x, y = queue.popleft()
        for dx, dy in grid.cardinal_directions:
            nx, ny = x + dx, y + dy
            # this adds one extra row and column around the outside of the squares
            if nx < -1 or ny < -1 or nx > len(tiles) or ny > len(tiles[0]):
                continue
            if grid.good_square(tiles, nx, ny) and tiles[nx][ny] == 1:
                continue
            if (nx, ny) in outside:
                continue

            outside.add((nx, ny))
            queue.append((nx, ny))

    return outside


def construct_prefix_sum_matrix(tiles: list[list[int]]) -> list[list[int]]:
    psm = [[0] * len(row) for row in tiles]

    for x in range(len(psm)):
        for y in range(len(psm[0])):
            psm[x][y] = tiles[x][y]
            psm[x][y] += psm[x - 1][y] if x > 0 else 0  # left
            psm[x][y] += psm[x][y - 1] if y > 0 else 0  # top
            psm[x][y] -= psm[x - 1][y - 1] if x > 0 and y > 0 else 0  # top left

    return psm


def valid_rectangle(psm: list[list[int]], xs: list[int], ys: list[int], corner1: tuple[int, int],
                    corner2: tuple[int, int]):
    cx1, cx2 = sorted([xs.index(corner1[0]) * 2, xs.index(corner2[0]) * 2])
    cy1, cy2 = sorted([ys.index(corner1[1]) * 2, ys.index(corner2[1]) * 2])

    left = psm[cx1 - 1][cy2] if cx1 > 0 else 0
    top = psm[cx2][cy1 - 1] if cy1 > 0 else 0
    top_left = psm[cx1 - 1][cy1 - 1] if cx1 > 0 and cy1 > 0 else 0

    count = psm[cx2][cy2] - left - top + top_left

    return count == area((cx1, cy1), (cx2, cy2))
