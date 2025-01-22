from collections import Counter

from util.grid import manhattan_distance


def solve_part1(lines: list[str]) -> int:
    center = (0, 0)

    wire1 = parse_wire_path(lines[0])
    wire2 = parse_wire_path(lines[1])
    intersections = find_intersections(wire1, wire2)

    for intersection in intersections:
        dist = manhattan_distance(intersection, center)
        intersections[intersection] = dist

    return min(intersections.values())


def solve_part2(lines: list[str]) -> int:
    wire1 = parse_wire_path(lines[0])
    wire2 = parse_wire_path(lines[1])
    intersections = find_intersections(wire1, wire2)

    for intersection in intersections:
        dist = distance_to_intersection(intersection, wire1)
        dist += distance_to_intersection(intersection, wire2)
        intersections[intersection] = dist

    return min(intersections.values())


def parse_wire_path(line: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    path = []
    start = end = (0, 0)
    directions = line.split(',')

    for d in directions:
        direction = d[0]
        length = int(d[1:])

        if direction == 'U':
            end = (start[0] + length, start[1])
        elif direction == 'R':
            end = (start[0], start[1] + length)
        elif direction == 'D':
            end = (start[0] - length, start[1])
        elif direction == 'L':
            end = (start[0], start[1] - length)

        path.append((start, end))
        start = end

    return path


def find_intersections(wire1, wire2) -> Counter:
    intersections = Counter()

    for w1 in wire1:
        for w2 in wire2:
            if w1[0] == (0, 0) and w2[0] == (0, 0):
                continue
            if (w1[0][0] == w1[1][0] and w2[0][0] == w2[1][0]) or (w1[0][1] == w1[1][1] and w2[0][1] == w2[1][1]):
                continue
            if w1[0][0] == w1[1][0]:
                if in_between(w1[0][0], w2[0][0], w2[1][0]) and in_between(w2[0][1], w1[0][1], w1[1][1]):
                    intersection = (w1[0][0], w2[0][1])
                    intersections[intersection] = 0
            else:
                if in_between(w1[0][1], w2[0][1], w2[1][1]) and in_between(w2[0][0], w1[0][0], w1[1][0]):
                    intersection = (w2[0][0], w1[0][1])
                    intersections[intersection] = 0

    return intersections


def distance_to_intersection(intersection: tuple[int, int],
                             wire_path: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    total = 0

    for segment in wire_path:
        if segment[0][0] == segment[1][0]:
            if intersection[0] == segment[0][0] and in_between(intersection[1], segment[0][1], segment[1][1]):
                total += abs(intersection[1] - segment[0][1])
                break
            else:
                total += abs(segment[0][1] - segment[1][1])
        else:
            if intersection[1] == segment[0][1] and in_between(intersection[0], segment[0][0], segment[1][0]):
                total += abs(intersection[0] - segment[0][0])
                break
            else:
                total += abs(segment[0][0] - segment[1][0])

    return total


def in_between(point: int, outer1: int, outer2: int) -> bool:
    min_o = min(outer1, outer2)
    max_o = max(outer1, outer2)

    return min_o <= point <= max_o
