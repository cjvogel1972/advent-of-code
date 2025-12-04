def solve_part1(lines: list[str]) -> int:
    banks = list(map(int, lines[0].split()))
    states = reallocation_loop(banks)

    return len(states)


def solve_part2(lines: list[str]) -> int:
    banks = list(map(int, lines[0].split()))
    states = reallocation_loop(banks)

    return len(states) - states.index(tuple(banks))


def reallocation_loop(banks: list[int]) -> list[tuple[int, ...]]:
    states = [tuple(banks)]

    while True:
        reallocate_banks(banks)

        if tuple(banks) in states:
            break
            
        states.append(tuple(banks))

    return states


def reallocate_banks(banks: list[int]):
    most_blocks = max(banks)
    index = banks.index(most_blocks)
    banks[index] = 0

    for i in range(1, most_blocks + 1):
        banks[(index + i) % len(banks)] += 1
