def solve_part1(lines: list[str]) -> int:
    instructions = [int(x) for x in lines]

    offset = 0
    jumps = 0

    while 0 <= offset < len(instructions):
        new_offset = offset + instructions[offset]
        instructions[offset] += 1
        jumps += 1
        offset = new_offset

    return jumps


def solve_part2(lines: list[str]) -> int:
    instructions = [int(x) for x in lines]

    offset = 0
    jumps = 0

    while 0 <= offset < len(instructions):
        new_offset = offset + instructions[offset]
        instructions[offset] += -1 if instructions[offset] >= 3 else 1
        jumps += 1
        offset = new_offset

    return jumps
