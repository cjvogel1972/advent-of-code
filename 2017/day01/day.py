def solve_part1(lines: list[str]) -> int:
    total = 0

    for i in range(len(lines[0])):
        next_index = i + 1 if i < len(lines[0]) - 1 else 0
        digit = lines[0][i]
        next_digit = lines[0][next_index]
        if digit == next_digit:
            total += int(digit)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    list_size = len(lines[0])
    size_half = list_size // 2
    for i in range(len(lines[0])):
        next_index = (i + size_half) % list_size
        digit = lines[0][i]
        next_digit = lines[0][next_index]
        if digit == next_digit:
            total += int(digit)

    return total
