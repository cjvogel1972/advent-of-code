from collections import Counter

VOWELS = ['a', 'e', 'i', 'o', 'u']
BAD_PAIRS = ['ab', 'cd', 'pq', 'xy']


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        if vowel_count(line) >= 3 and has_double_letters(line) and not has_bad_pairs(line):
            total += 1

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        if has_duplicating_pair(line) and has_repeat_with_letter_between(line):
            total += 1

    return total


def vowel_count(word: str) -> int:
    letter_count = Counter(word)

    count = 0
    for vowel in VOWELS:
        count += letter_count[vowel]

    return count


def has_double_letters(word: str) -> bool:
    for a, b in zip(word, word[1:]):
        if a == b:
            return True

    return False


def has_bad_pairs(word: str) -> bool:
    for pair in BAD_PAIRS:
        if pair in word:
            return True

    return False


def has_duplicating_pair(word: str) -> bool:
    for i in range(len(word) - 2):
        pair = word[i] + word[i + 1]
        if pair in word[i + 2:]:
            return True

    return False


def has_repeat_with_letter_between(word: str) -> bool:
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            return True

    return False
