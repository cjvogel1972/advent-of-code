from collections import Counter


def solve_part1(lines: list[str]) -> str:
    program_weights, program_dependencies = parse_information(lines)

    return determine_bottom_program(program_dependencies, program_weights)


def solve_part2(lines: list[str]) -> int:
    program_weights, program_dependencies = parse_information(lines)

    bottom_program = determine_bottom_program(program_dependencies, program_weights)

    unbalanced_program, goal_weight, _ = unbalanced_program_and_weights(bottom_program,
                                                                        program_dependencies,
                                                                        program_weights)

    return updated_weight(goal_weight, unbalanced_program, program_dependencies, program_weights)


def parse_information(lines: list[str]) -> tuple[dict[str, int], dict[str, set[str]]]:
    program_weights: dict[str, int] = {}
    program_dependencies: dict[str, set[str]] = {}

    for line in lines:
        info = line.split(" ")
        program_name = info[0]
        program_weights[program_name] = int(info[1][1:-1])

        if " -> " in line:
            deps = line.split(" -> ")[1]
            program_dependencies[program_name] = set(deps.split(", "))

    return program_weights, program_dependencies


def determine_bottom_program(dependencies: dict[str, set[str]], weights: dict[str, int]) -> str:
    programs = set(weights.keys())
    dependencies: set[str] = {dep for deps in dependencies.values() for dep in deps}

    return (programs - dependencies).pop()


def unbalanced_program_and_weights(bottom_program: str, dependencies: dict[str, set[str]],
                                   weights: dict[str, int]) -> tuple[str, int, int]:
    weights = {pgm: tower_weight(pgm, dependencies, weights) for pgm in dependencies[bottom_program]}

    weight_counts = Counter(list(weights.values())).most_common()
    goal_weight = weight_counts[0][0]
    unbalanced_weight = 0 if len(weight_counts) == 1 else weight_counts[-1][0]

    program = find_program_with_weight(weights, unbalanced_weight)

    return program, goal_weight, unbalanced_weight


def updated_weight(goal_weight: int, program: str, dependencies: dict[str, set[str]],
                   weights: dict[str, int]) -> int:
    if program in dependencies:
        new_program, new_goal, new_unbalanced_weight = unbalanced_program_and_weights(program, dependencies, weights)

        if new_unbalanced_weight == 0:
            return goal_weight - (new_goal * len(dependencies[program]))
        else:
            return updated_weight(new_goal, new_program, dependencies, weights)
    else:
        return goal_weight


def tower_weight(program: str, dependencies: dict[str, set[str]], weights: dict[str, int]) -> int:
    weight = weights[program]

    if program in dependencies:
        weight += sum([tower_weight(dep, dependencies, weights) for dep in dependencies[program]])

    return weight


def find_program_with_weight(weights: dict[str, int], weight) -> str:
    for key, val in weights.items():
        if val == weight:
            return key

    return None
