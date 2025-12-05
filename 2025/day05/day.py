def solve_part1(lines: list[str]) -> int:
    line_no, ranges = parse_ranges(lines)

    fresh = 0
    while line_no < len(lines):
        ingredient = int(lines[line_no])
        for r in ranges:
            if r[0] <= ingredient <= r[1]:
                fresh += 1
                break
        line_no += 1

    return fresh


def solve_part2(lines: list[str]) -> int:
    _, ranges = parse_ranges(lines)
    merged_ranges = merge_ranges(ranges)

    fresh = 0

    for r in merged_ranges:
        fresh += r[1] - r[0] + 1

    return fresh


def parse_ranges(lines: list[str]) -> tuple[int, list[tuple[int, int]]]:
    ranges: list[tuple[int, int]] = []

    line_no = 0
    while lines[line_no]:
        r = tuple(map(int, lines[line_no].split('-')))
        ranges.append(r)
        line_no += 1

    line_no += 1

    return line_no, ranges


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ranges.sort()

    merged_ranges: list[tuple[int, int]] = []
    i = 0
    while i < len(ranges):
        r_min, r_max = ranges[i]
        while i + 1 < len(ranges):
            next_min, next_max = ranges[i + 1]
            if r_min <= next_min <= r_max:
                r_max = max(r_max, next_max)
                i += 1
            else:
                break
        i += 1

        merged_ranges.append((r_min, r_max))
    return merged_ranges
