import json


def solve_part1(lines: list[str]) -> int:
    data = json.loads(lines[0])
    ignore_red = False

    return sum_value(data, ignore_red)


def solve_part2(lines: list[str]) -> int:
    data = json.loads(lines[0])
    ignore_red = True

    return sum_value(data, ignore_red)


def sum_value(value, ignore_red: bool) -> int:
    total = 0

    if isinstance(value, int):
        total += value
    elif isinstance(value, dict):
        total += sum_dictionary(value, ignore_red)
    elif isinstance(value, list):
        total += sum_list(value, ignore_red)

    return total

def sum_dictionary(data: dict, ignore_red: bool) -> int:
    values = data.values()
    if ignore_red and "red" in values:
        return 0

    total = 0
    for value in values:
        total += sum_value(value, ignore_red)

    return total

def sum_list(data: list, ignore_red: bool) -> int:
    total = 0

    for value in data:
        total += sum_value(value, ignore_red)

    return total