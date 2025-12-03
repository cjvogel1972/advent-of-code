def solve_part1(lines: list[str]) -> int:
    total_joltage = 0

    for line in lines:
        total_joltage += max_joltage_for_bank(line, 2)

    return total_joltage


def solve_part2(lines: list[str]) -> int:
    total_joltage = 0

    for line in lines:
        total_joltage += max_joltage_for_bank(line, 12)

    return total_joltage


def max_joltage_for_bank(battery_bank: str, num_batteries: int) -> int:
    max_joltage = ""
    start = 0

    for i in range(num_batteries):
        end = num_batteries - i - 1
        bank = battery_bank[start:-end] if end > 0 else battery_bank[start:]
        battery, slot = largest_battery(bank)
        start += slot + 1
        max_joltage += battery

    return int(max_joltage)


def largest_battery(battery_bank: str) -> tuple[str, int]:
    battery_joltage = 0
    slot = 0
    
    for i in range(len(battery_bank)):
        joltage = int(battery_bank[i])
        if joltage > battery_joltage:
            battery_joltage = joltage
            slot = i

    return battery_bank[slot], slot
