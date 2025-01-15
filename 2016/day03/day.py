def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        if is_valid_triangle(list(map(int, line.strip().split()))):
            total += 1

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for i in range(0, len(lines), 3):
        nums = []
        for j in range(i, i + 3):
            nums.append(list(map(int, lines[j].strip().split())))
        for a, b, c in zip(*nums):
            if is_valid_triangle([a, b, c]):
                total += 1

    return total


def is_valid_triangle(nums: list[int]) -> bool:
    a, b, c = tuple(sorted(nums))
    if a + b > c:
        return True

    return False
