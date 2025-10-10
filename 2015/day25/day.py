def solve_part1(lines: list[str]) -> int:
    row = 2981
    column = 3075

    count = compute_number_of_cells(column, row)

    code = 20151125
    for i in range(count):
        code = next_code(code)

    return code


def compute_number_of_cells(column: int, row: int) -> int:
    count = 0

    for i in range(2, row + column - 1):
        count += i
    count += column

    return count


def next_code(code: int) -> int:
    return (code * 252533) % 33554393


def solve_part2(lines: list[str]) -> int:
    return 0
