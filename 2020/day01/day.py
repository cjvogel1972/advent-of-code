def solve_part1(lines: list[str]) -> int:
    expenses = list(map(int, lines))

    for i in range(len(expenses) - 1):
        for j in range(i + 1, len(expenses)):
            if expenses[i] + expenses[j] == 2020:
                return expenses[i] * expenses[j]

    return -1


def solve_part2(lines: list[str]) -> int:
    expenses = list(map(int, lines))

    for i in range(len(expenses) - 2):
        for j in range(i + 1, len(expenses) - 1):
            for k in range(j + 1, len(expenses)):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i] * expenses[j] * expenses[k]

    return -1
