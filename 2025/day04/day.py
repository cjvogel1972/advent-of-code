from util.grid import good_square, directions


def solve_part1(lines: list[str]) -> int:
    accessible_paper = 0

    room_length = len(lines)
    room_width = len(lines[0])

    grid = [list(line) for line in lines]

    for y in range(room_length):
        for x in range(room_width):
            if grid[y][x] == "@":
                if paper_around(grid, x, y) < 4:
                    accessible_paper += 1

    return accessible_paper


def solve_part2(lines: list[str]) -> int:
    rolls_removed = 0

    room_length = len(lines)
    room_width = len(lines[0])

    grid = [list(line) for line in lines]

    while True:
        paper_removed = False
        for y in range(room_length):
            for x in range(room_width):
                if grid[y][x] == "@":
                    if paper_around(grid, x, y) < 4:
                        grid[y][x] = "."
                        rolls_removed += 1
                        paper_removed = True

        if not paper_removed:
            break

    return rolls_removed


def paper_around(grid: list[list[str]], x: int, y: int) -> int:
    rolls = 0

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy
        if good_square(grid, new_y, new_x):
            rolls += 1 if grid[new_y][new_x] == "@" else 0

    return rolls
