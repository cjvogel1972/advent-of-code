def solve_part1(lines: list[str]) -> int:
    operators = lines[-1].split()
    numbers = [list(map(int, lines[i].split())) for i in range(len(lines) - 1)]

    total = 0
    for i in range(len(numbers[0])):
        nums = [numbers[j][i] for j in range(len(numbers))]
        total += compute_answer(nums, operators[i])

    return total


def solve_part2(lines: list[str]) -> int:
    operators = lines[-1]

    total = 0

    start = 0
    next_op_idx = 0
    while next_op_idx != -1:
        next_op_idx = find_next_operator(operators, start)
        end = len(operators) if next_op_idx == -1 else next_op_idx - 1
        numbers = parse_numbers(lines, start, end)

        total += compute_answer(numbers, operators[start])
        start = next_op_idx

    return total


def compute_answer(numbers: list[int], operator: str) -> int:
    solution = 0 if operator == '+' else 1

    for n in numbers:
        if operator == '+':
            solution += n
        else:
            solution *= n

    return solution


def find_next_operator(line: str, start_index: int) -> int:
    plus = line.find('+', start_index + 1)
    times = line.find('*', start_index + 1)

    if plus == -1 and times == -1:
        return -1
    elif plus == -1:
        return times
    elif times == -1:
        return plus
    else:
        return min(plus, times)


def parse_numbers(lines: list[str], start: int, end: int) -> list[int]:
    numbers = []

    for i in range(start, end):
        n = ""
        for j in range(len(lines) - 1):
            n += lines[j][i]

        numbers.append(int(n))

    return numbers
