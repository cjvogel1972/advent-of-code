from collections import defaultdict


def solve_part1(lines: list[str]) -> int:
    beams: set[int] = {find_start(lines)}
    split = 0

    for i in range(1, len(lines)):
        if "^" not in lines[i]:
            continue

        new_beams: set[int] = set()
        for beam in beams:
            if lines[i][beam] == "^":
                split += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)

        beams = new_beams

    return split


def solve_part2(lines: list[str]) -> int:
    beams = defaultdict(int)
    beams[find_start(lines)] = 1

    for i in range(1, len(lines)):
        if "^" not in lines[i]:
            continue

        new_beams = defaultdict(int)
        for beam in beams.keys():
            if lines[i][beam] == "^":
                new_beams[beam - 1] += beams[beam]
                new_beams[beam + 1] += beams[beam]
            else:
                new_beams[beam] += beams[beam]

        beams = new_beams

    return sum(beams.values())


def find_start(lines: list[str]) -> int:
    return lines[0].find("S")
