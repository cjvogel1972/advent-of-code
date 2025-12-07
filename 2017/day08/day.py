from collections import defaultdict


def solve_part1(lines: list[str]) -> int:
    registers = defaultdict(int)

    for line in lines:
        instruction = line.split()

        if check_condition(registers, instruction[4:7]):
            perform_op(registers, instruction[0:3])

    return max(list(registers.values()))


def solve_part2(lines: list[str]) -> int:
    registers = defaultdict(int)
    max_value = 0

    for line in lines:
        instruction = line.split()

        if check_condition(registers, instruction[4:7]):
            perform_op(registers, instruction[0:3])

        max_value = max(max_value, registers[instruction[0]])

    return max_value


def check_condition(registers: dict, condition: list[str]) -> bool:
    condition_reg = registers[condition[0]]
    cond = condition[1]
    condition_val = int(condition[2])

    result = False
    if cond == "==":
        result = condition_reg == condition_val
    elif cond == "!=":
        result = condition_reg != condition_val
    elif cond == ">":
        result = condition_reg > condition_val
    elif cond == "<":
        result = condition_reg < condition_val
    elif cond == ">=":
        result = condition_reg >= condition_val
    elif cond == "<=":
        result = condition_reg <= condition_val

    return result


def perform_op(registers: dict, instruction: list[str]):
    reg = instruction[0]
    op = instruction[1]
    value = int(instruction[2])

    if op == "inc":
        registers[reg] += value
    else:
        registers[reg] -= value
