def solve_part1(lines: list[str]) -> int:
    valid_count = 0

    for line in lines:
        if valid_passphrase(line):
            valid_count += 1

    return valid_count


def solve_part2(lines: list[str]) -> int:
    valid_count = 0

    for line in lines:
        if valid_passphrase_no_anagrams(line):
            valid_count += 1

    return valid_count


def valid_passphrase(line: str) -> bool:
    words = line.split(' ')

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                return False

    return True


def valid_passphrase_no_anagrams(line: str) -> bool:
    words = line.split(' ')

    for i in range(len(words) - 1):
        letters = sorted(words[i])
        for j in range(i + 1, len(words)):
            if letters == sorted(words[j]):
                return False

    return True
