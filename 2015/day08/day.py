def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        decoded_line = line.encode('ascii', 'ignore').decode('unicode_escape')
        total += len(line) - (len(decoded_line) - 2)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        decoded_line = line.encode('unicode_escape', 'ignore').decode('ascii')
        decoded_len = len(decoded_line) + decoded_line.count('"') + 2
        total += decoded_len - len(line)

    return total
