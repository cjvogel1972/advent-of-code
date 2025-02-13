def solve_part1(lines: list[str]) -> int:
    replacements, medicine = parse_input(lines)

    results = set()

    i = 0
    while i < len(medicine):
        if medicine[i] in replacements:
            for r in replacements[medicine[i]]:
                new_medicine = medicine[:i] + r + medicine[i + 1:]
                results.add(new_medicine)
        elif medicine[i:i + 2] in replacements:
            for r in replacements[medicine[i:i + 2]]:
                new_medicine = medicine[:i] + r + medicine[i + 2:]
                results.add(new_medicine)
        i += 1

    return len(results)


def solve_part2(lines: list[str]) -> int:
    replacements, medicine = parse_input(lines)

    reverse_replacements = {}
    for atom, rs in replacements.items():
        for r in rs:
            reverse_replacements[r] = atom

    steps = 0
    current_medicine = medicine

    modified = True
    while modified:
        modified = False
        for molecule, atom in reverse_replacements.items():
            if molecule not in current_medicine:
                continue

            modified = True
            current_medicine = current_medicine.replace(molecule, atom, 1)
            steps += 1

    return steps if current_medicine == "e" else -1


def parse_input(lines: list[str]) -> tuple[dict[str, list[str]], str]:
    replacements = {}
    i = 0

    while True:
        if lines[i].strip() == "":
            break

        molecule1, _, molecule2 = lines[i].split()
        if molecule1 not in replacements:
            replacements[molecule1] = []
        replacements[molecule1].append(molecule2)
        i += 1

    medicine = lines[i + 1]

    return replacements, medicine
