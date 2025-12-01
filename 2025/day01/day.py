def solve_part1(lines: list[str]) -> int:
    dial = 50
    password = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])
        dial += clicks if direction == "R" else -clicks
        dial %= 100

        if dial == 0:
            password += 1

    return password


def solve_part2(lines: list[str]) -> int:
    dial = 50
    password = 0

    for line in lines:
        start = dial
        direction = line[0]
        clicks = int(line[1:])
        dial += clicks if direction == "R" else -clicks
        end = dial
        dial %= 100

        if end < 0:
            password += (abs(end) // 100) + (0 if start == 0 else 1)
        elif end > 100:
            password += (end // 100)
        elif dial == 0:
            password += 1

    return password
