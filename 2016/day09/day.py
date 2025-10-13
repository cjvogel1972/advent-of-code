def solve_part1(lines: list[str]) -> int:
    return len(decompress(lines[0], 1))


def solve_part2(lines: list[str]) -> int:
    return len(decompress(lines[0], 2))


def decompress(line: str, version: int) -> str:
    result = ""

    pointer = 0
    while pointer < len(line):
        open_paren_loc = line.find("(", pointer)
        if open_paren_loc == -1:
            result += line[pointer:]
            break

        result += line[pointer:open_paren_loc]
        close_paren_loc = line.find(")", open_paren_loc)
        marker = line[open_paren_loc + 1:close_paren_loc]
        num_chars, repeat = map(int, marker.split("x"))
        sequence = line[close_paren_loc + 1:close_paren_loc + 1 + num_chars]
        if version == 1:
            result += sequence * repeat
        else:
            result += decompress(sequence, version) * repeat

        pointer = close_paren_loc + 1 + num_chars

    return result
