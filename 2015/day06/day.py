import re

PARSER = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')


def solve_part1(lines: list[str]) -> int:
    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        rule, y1, x1, y2, x2 = parse_line(line)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if rule == 'toggle':
                    lights[y][x] = not lights[y][x]
                else:
                    lights[y][x] = True if rule == 'turn on' else False

    return sum(sum(row) for row in lights)


def solve_part2(lines: list[str]) -> int:
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        rule, y1, x1, y2, x2 = parse_line(line)
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if rule == 'toggle':
                    lights[y][x] += 2
                else:
                    lights[y][x] += 1 if rule == 'turn on' else -1
                    if lights[y][x] < 0:
                        lights[y][x] = 0

    return sum(sum(row) for row in lights)


def parse_line(line: str) -> tuple[str, int, int, int, int]:
    rule, y1, x1, y2, x2 = PARSER.search(line).groups()
    y1 = int(y1)
    y2 = int(y2)
    x1 = int(x1)
    x2 = int(x2)

    return rule, y1, x1, y2, x2