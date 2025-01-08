from collections import Counter


def solve_part1(lines: list[str]) -> int:
    result = 0

    for line in lines:
        min_count, max_count, letter, password = parse_policy_password(line)

        char_count = Counter(password)
        count = char_count[letter]
        if min_count <= count <= max_count:
            result += 1

    return result


def solve_part2(lines: list[str]) -> int:
    result = 0

    for line in lines:
        left, right, letter, password = parse_policy_password(line)
        left -= 1
        right -= 1

        if (password[left] == letter and password[right] != letter) or (
                password[left] != letter and password[right] == letter):
            result += 1

    return result


def parse_policy_password(line):
    policy, password = line.split(": ")
    times, letter = policy.split(" ")
    left, right = map(int, times.split("-"))

    return left, right, letter, password
