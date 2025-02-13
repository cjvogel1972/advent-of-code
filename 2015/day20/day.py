import math


def solve_part1(lines: list[str]) -> int:
    present_goal = int(lines[0])

    house_no = 0
    while True:
        house_no += 1
        presents = presents_for_house_infinite_visits(house_no)
        if presents >= present_goal:
            break

    return house_no


def solve_part2(lines: list[str]) -> int:
    present_goal = int(lines[0])

    house_no = 0
    while True:
        house_no += 1
        presents = presents_for_house_fifty_visits(house_no)
        if presents >= present_goal:
            break

    return house_no


def presents_for_house_infinite_visits(house_no: int) -> int:
    visiting_elfs = get_factors(house_no)
    return sum(visiting_elfs) * 10


def presents_for_house_fifty_visits(house_no: int) -> int:
    visiting_elfs = get_factors(house_no)

    presents = 0
    for elf_no in visiting_elfs:
        if house_no // elf_no <= 50:
            presents += elf_no

    return presents * 11


def get_factors(number):
    factors = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            if number // i != i:
                factors.append(number // i)

    factors.sort()
    return factors
