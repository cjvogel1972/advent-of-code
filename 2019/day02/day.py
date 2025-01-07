def solve_part1(lines: list[str]) -> int:
    codes = list(map(int, lines[0].split(',')))
    codes[1] = 12
    codes[2] = 2

    return run_program(codes)


def solve_part2(lines: list[str]) -> int:
    for noun in range(100):
        for verb in range(100):
            codes = list(map(int, lines[0].split(',')))
            codes[1] = noun
            codes[2] = verb

            if run_program(codes) == 19690720:
                break
        else:
            continue
        break

    return (100 * noun) + verb


def run_program(codes: list[int]) -> int:
    ptr = 0
    while ptr < len(codes):
        opcode = codes[ptr]
        if opcode == 99:
            break
        if opcode == 1:
            codes[codes[ptr + 3]] = codes[codes[ptr + 1]] + codes[codes[ptr + 2]]
        elif opcode == 2:
            codes[codes[ptr + 3]] = codes[codes[ptr + 1]] * codes[codes[ptr + 2]]
        ptr += 4

    return codes[0]
