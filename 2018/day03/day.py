import re
from collections import namedtuple, Counter

Point = namedtuple('Point', ['x', 'y'])
Rectangle = namedtuple('Rectangle', ['c1', 'c2'])


def solve_part1(lines: list[str]) -> int:
    claims = []
    pattern = re.compile("#\d+ @ (\d+),(\d+): (\d+)x(\d+)")
    for line in lines:
        x, y, dx, dy = map(int, pattern.search(line).groups())
        claims.append(Rectangle(Point(x, y), Point(x + dx, y + dy)))

    squares = Counter()
    for claim in claims:
        for x in range(claim.c1.x, claim.c2.x):
            for y in range(claim.c1.y, claim.c2.y):
                squares[(x, y)] += 1

    total = 0
    for c in squares.values():
        if c > 1:
            total += 1

    return total


def solve_part2(lines: list[str]) -> int:
    claims = {}
    pattern = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    for line in lines:
        num, x, y, dx, dy = map(int, pattern.search(line).groups())
        claims[num] = Rectangle(Point(x, y), Point(x + dx, y + dy))

    nums = list(claims.keys())
    for i, n in enumerate(nums):
        has_overlaps = False
        for j, n2 in enumerate(nums):
            if i == j:
                continue
            if overlap(claims[n], claims[n2]):
                has_overlaps = True

        if not has_overlaps:
            return n

    return 0


def overlap(rect1: Rectangle, rect2: Rectangle) -> bool:
    if rect1.c1.x >= rect2.c2.x or rect2.c1.x >= rect1.c2.x:
        return False

    if rect1.c2.y <= rect2.c1.y or rect2.c2.y <= rect1.c1.y:
        return False

    return True
