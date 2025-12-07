def solve_part1(lines: list[str]) -> int:
    return score_groups(lines[0])


def solve_part2(lines: list[str]) -> int:
    return count_garbage(lines[0])


def score_groups(stream: str) -> int:
    score, _, _ = parse_group(stream, -1)

    return score


def count_garbage(stream: str) -> int:
    _, garbage_count, _ = parse_group(stream, -1)

    return garbage_count


def parse_group(stream: str, outer_score: int) -> tuple[int, int, int]:
    garbage_char_count = 0
    score = outer_score + 1
    i = 0

    while i < len(stream) and stream[i] != "}":
        move = 0
        garbage_count = 0
        if stream[i] == "<":
            garbage_count, move = parse_garbage(stream[i + 1:])
        elif stream[i] == "{":
            sub_score, garbage_count, move = parse_group(stream[i + 1:], outer_score + 1)
            score += sub_score

        garbage_char_count += garbage_count
        i += 1 + move

    return score, garbage_char_count, i + 1


def parse_garbage(stream: str) -> tuple[int, int]:
    character_count = 0
    i = 0

    while i < len(stream) and stream[i] != ">":
        if stream[i] == "!":
            i += 1
        else:
            character_count += 1

        i += 1

    return character_count, i + 1
