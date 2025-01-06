from collections import Counter


def solve_part1(lines: list[str]) -> int:
    two_letter_count = 0
    three_letter_count = 0

    for line in lines:
        letters = Counter(line)
        two_found = False
        three_found = False
        for letter, count in letters.items():
            if count == 2 and not two_found:
                two_letter_count += 1
                two_found = True
                continue
            if count == 3 and not three_found:
                three_letter_count += 1
                three_found = True
                continue

    return two_letter_count * three_letter_count


def solve_part2(lines: list[str]) -> int:
    correct_ids = []
    for i, line in enumerate(lines):
        for line2 in lines[i + 1:]:
            diff_count = 0
            for a, b in zip(line, line2):
                if a != b:
                    diff_count += 1
            if diff_count == 1:
                correct_ids.append(line)
                correct_ids.append(line2)

    result = ""
    for a, b in zip(*correct_ids):
        if a == b:
            result += a

    return result
