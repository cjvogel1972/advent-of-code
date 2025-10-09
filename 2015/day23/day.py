def solve_part1(lines: list[str]) -> int:
    reg_a, reg_b = run_program(lines, 0, 0)

    return reg_b


def solve_part2(lines: list[str]) -> int:
    reg_a, reg_b = run_program(lines, 1, 0)

    return reg_b


def run_program(lines: list[str], reg_a: int, reg_b: int) -> tuple[int, int]:
    ptr = 0

    while 0 <= ptr < len(lines):
        line = lines[ptr]
        instruction = line[:3]
        register = line[4]

        if instruction == 'hlf':
            if register == 'a':
                reg_a = reg_a // 2
            elif register == 'b':
                reg_b = reg_b // 2

            ptr += 1
        elif instruction == 'tpl':
            if register == 'a':
                reg_a *= 3
            elif register == 'b':
                reg_b *= 3

            ptr += 1
        elif instruction == 'inc':
            if register == 'a':
                reg_a += 1
            elif register == 'b':
                reg_b += 1

            ptr += 1
        elif instruction == 'jmp':
            offset = int(line[4:])

            ptr += offset
        elif instruction == 'jie':
            offset = int(line[7:])

            if register == 'a' and reg_a % 2 == 0:
                ptr += offset
            elif register == 'b' and reg_b % 2 == 0:
                ptr += offset
            else:
                ptr += 1
        elif instruction == 'jio':
            offset = int(line[7:])
            
            if register == 'a' and reg_a == 1:
                ptr += offset
            elif register == 'b' and reg_b == 1:
                ptr += offset
            else:
                ptr += 1

    return reg_a, reg_b
