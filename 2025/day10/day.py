import sys
from collections import deque
from scipy.optimize import linprog


def solve_part1(lines: list[str]) -> int:
    button_presses = 0

    for line in lines:
        expected_lights, buttons, _ = parse_machine_info(line)
        lights = "." * len(expected_lights)

        seen_button_count = {lights: 0}
        queue = deque([lights])

        while queue:
            l = queue.popleft()
            count = seen_button_count[l] + 1
            for b in buttons:
                new_lights = push_button_for_lights(l, b)
                if new_lights not in seen_button_count:
                    seen_button_count[new_lights] = count
                    queue.append(new_lights)

        button_presses += seen_button_count[expected_lights]

    return button_presses


def solve_part2(lines: list[str]) -> int:
    button_presses = 0

    for line in lines:
        _, buttons, expected_joltage = parse_machine_info(line)

        button_presses += compute_minimum_button_pushes(expected_joltage, buttons)

    return button_presses


def parse_machine_info(line: str) -> tuple[str, list[list[int]], list[int]]:
    parts = line.split()

    expected_lights = parts[0][1:-1]
    buttons: list[list[int]] = [list(map(int, parts[i][1:-1].split(","))) for i in range(1, len(parts) - 1)]
    expected_joltage: list[int] = list(map(int, parts[-1][1:-1].split(",")))

    return expected_lights, buttons, expected_joltage


def push_button_for_lights(lights: str, button_wiring: list[int]) -> str:
    new_lights = ""

    for i, c in enumerate(lights):
        if i in button_wiring:
            if c == ".":
                new_lights += "#"
            else:
                new_lights += "."
        else:
            new_lights += c

    return new_lights


def compute_minimum_button_pushes(expected_joltage: list[int], button_wiring: list[list[int]]) -> int:
    objective_function = [1] * len(button_wiring)
    integrality = [1] * len(button_wiring)

    lhs_eq = [[0 for _ in range(len(button_wiring))] for _ in range(len(expected_joltage))]
    for i, wiring in enumerate(button_wiring):
        for w in wiring:
            lhs_eq[w][i] = 1

    bnd = [(0, sys.maxsize)] * len(button_wiring)
    opt = linprog(c=objective_function, A_eq=lhs_eq, b_eq=expected_joltage, bounds=bnd, integrality=integrality, method="highs")

    return int(opt.fun)
