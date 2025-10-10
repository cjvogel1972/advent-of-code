import math


def solve_part1(lines: list[str]) -> int:
    return balance_packages(lines, 3)


def solve_part2(lines: list[str]) -> int:
    return balance_packages(lines, 4)


def balance_packages(lines: list[str], num_groups: int) -> int:
    package_weights = [int(x) for x in lines]
    ideal_weight = sum(package_weights) // num_groups
    package_weights.sort(reverse=True)

    options = find_package_combinations_equal_to_expected_weight(ideal_weight, package_weights)
    min_num_packages = min([len(option) for option in options])
    best_options = [option for option in options if len(option) == min_num_packages]

    best_quantum_entanglement = min([compute_quantum_entanglement(p) for p in best_options])
    return best_quantum_entanglement


def find_package_combinations_equal_to_expected_weight(expected_weight: int, packages: list[int]) -> list[list[int]]:
    results = []

    index = 0
    while index < len(packages):
        if packages[index] == expected_weight:
            results.append([packages[index]])
        if packages[index] < expected_weight:
            new_combinations = find_package_combinations_equal_to_expected_weight(expected_weight - packages[index],
                                                                                  packages[index + 1:])
            for combination in new_combinations:
                combination.insert(0, packages[index])
                results.append(combination)

        index += 1

    return results


def compute_quantum_entanglement(packages: list[int]) -> int:
    return math.prod(packages)
