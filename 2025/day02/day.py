def solve_part1(lines: list[str]) -> int:
    invalid = 0

    ranges = lines[0].split(',')

    for r in ranges:
        start, end = tuple(map(int, r.split('-')))
        for n in range(start, end + 1):
            if not is_valid_id_part1(str(n)):
                invalid += n

    return invalid


def solve_part2(lines: list[str]) -> int:
    invalid = 0

    ranges = lines[0].split(',')

    for r in ranges:
        start, end = tuple(map(int, r.split('-')))
        for n in range(start, end + 1):
            if not is_valid_id_part2(str(n)):
                invalid += n

    return invalid


def is_valid_id_part1(product_id: str) -> bool:
    l = len(product_id)
    if l % 2 == 0:
        return not product_id[:l // 2] == product_id[l // 2:]

    return True


def is_valid_id_part2(product_id: str) -> bool:
    l = len(product_id)
    for i in range(1, (l // 2) + 1):
        if l % i == 0 and product_id[:i] * (l // i) == product_id:
            return False

    return True
