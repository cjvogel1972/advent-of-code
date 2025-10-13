import re


def solve_part1(lines: list[str]) -> int:
    screen = build_screen(50, 6)
    screen = run_instructions(lines, screen)

    return count_lit_pixels(screen)


def solve_part2(lines: list[str]) -> int:
    screen = build_screen(50, 6)
    screen = run_instructions(lines, screen)

    print_screen(screen)

    return 0


def build_screen(width: int, height: int) -> list[list[str]]:
    return [["." for _ in range(width)] for _ in range(height)]


def run_instructions(instructions: list[str], screen: list[list[str]]) -> list[list[str]]:
    for instruction in instructions:
        match = re.match(r"rect (\d+)x(\d+)", instruction)
        if match:
            a, b = map(int, match.groups())
            screen = rect(a, b, screen)
            continue

        match = re.match(r"rotate row y=(\d+) by (\d+)", instruction)
        if match:
            y, by = map(int, match.groups())
            screen = rotate_row(y, by, screen)
            continue

        match = re.match(r"rotate column x=(\d+) by (\d+)", instruction)
        if match:
            x, by = map(int, match.groups())
            screen = rotate_column(x, by, screen)
            continue

    return screen


def count_lit_pixels(screen: list[list[str]]) -> int:
    return sum(1 for y in range(len(screen)) for x in range(len(screen[0])) if screen[y][x] == "#")


def print_screen(screen: list[list[str]]):
    for row in screen:
        print("".join(row))
    print()


def rect(a: int, b: int, screen: list[list[str]]) -> list[list[str]]:
    for y in range(b):
        for x in range(a):
            screen[y][x] = "#"

    return screen


def rotate_row(y: int, by: int, screen: list[list[str]]) -> list[list[str]]:
    screen[y] = screen[y][-by:] + screen[y][:-by]

    return screen


def rotate_column(x: int, by: int, screen: list[list[str]]) -> list[list[str]]:
    column = [screen[y][x] for y in range(len(screen))]
    column = column[-by:] + column[:-by]
    for y in range(len(screen)):
        screen[y][x] = column[y]

    return screen
