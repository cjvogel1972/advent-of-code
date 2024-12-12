def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        mass = int(line)
        total += compute_fuel(mass)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        mass = int(line)
        fuel = compute_fuel(mass)
        while fuel > 0:
            total += fuel
            fuel = compute_fuel(fuel)

    return total


def compute_fuel(mass: int) -> int:
    return mass // 3 - 2
