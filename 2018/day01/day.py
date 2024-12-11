def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        if line[0] == "+":
            total += int(line[1:])
        else:
            total += int(line)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    found_frequencies = set()
    found_frequencies.add(0)
    while True:
        for line in lines:
            if line[0] == "+":
                total += int(line[1:])
            else:
                total += int(line)
            if total in found_frequencies:
                break
            found_frequencies.add(total)
        else:
            continue
        break

    return total
