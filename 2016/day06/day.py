from collections import defaultdict


def solve_part1(lines: list[str]) -> str:
    position_counters = count_letters_in_positions(lines)

    return "".join([max(counters, key=counters.get) for counters in position_counters])


def solve_part2(lines: list[str]) -> str:
    position_counters = count_letters_in_positions(lines)

    return "".join([min(counters, key=counters.get) for counters in position_counters])


def count_letters_in_positions(lines: list[str]) -> list[defaultdict[str, int]]:
    position_counters = [defaultdict(int) for _ in range(len(lines[0]))]
    for line in lines:
        for i, c in enumerate(line):
            position_counters[i][c] += 1
    return position_counters
