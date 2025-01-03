def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        nums = list(map(int, line.split()))
        biggest_diff = 0
        for i, x in enumerate(nums):
            for y in nums[i + 1:]:
                biggest_diff = max(biggest_diff, abs(x - y))
        total += biggest_diff

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        nums = list(map(int, line.split()))
        result = 0
        for i, x in enumerate(nums):
            for y in nums[i + 1:]:
                if x % y == 0:
                    result = x // y
                elif y % x == 0:
                    result = y // x
        total += result

    return total
