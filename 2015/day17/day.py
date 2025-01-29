from collections import Counter


def solve_part1(lines: list[str]) -> int:
    containers = [int(line) for line in lines]

    result = fill_containers(containers, 150)

    return len(result)


def solve_part2(lines: list[str]) -> int:
    containers = [int(line) for line in lines]

    result = fill_containers(containers, 150)

    return count_minimum_containers(result)


def fill_containers(containers: list[int], liters_remaining: int) -> list[list[int]]:
    result = []
    for i, container in enumerate(containers):
        if container > liters_remaining:
            continue

        sub_result = []
        if container < liters_remaining:
            if len(containers) > i + 1:
                sub_result = fill_containers(containers[i + 1:], liters_remaining - container)
            else:
                break

        if len(sub_result) == 0 and container == liters_remaining:
            result.append([container])
        else:
            for r in sub_result:
                r.insert(0, container)
            for r in sub_result:
                if sum(r) == liters_remaining:
                    result.append(r)

    return result

def count_minimum_containers(container_combinations: list[list[int]]) -> int:
    container_counts = Counter()
    min_containers = float("inf")

    for combination in container_combinations:
        num_containers = len(combination)
        container_counts[num_containers] += 1
        min_containers = min(min_containers, num_containers)

    return container_counts[min_containers]
