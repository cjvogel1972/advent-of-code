from math import sqrt
from typing import NamedTuple


def solve_part1(lines: list[str]) -> int:
    return make_x_connections(1000, lines)


def solve_part2(lines: list[str]) -> int:
    return make_full_circuit(lines)


class Coordinate(NamedTuple):
    x: int
    y: int
    z: int


def make_x_connections(num_connections: int, lines: list[str]) -> int:
    junction_boxes = parse_junction_boxes(lines)
    connections = calculate_connection_distances(junction_boxes)

    circuits: list[list[Coordinate]] = []

    for _ in range(num_connections):
        make_smallest_connection(circuits, connections)

    circuits.sort(key=lambda c: len(c), reverse=True)

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def make_full_circuit(lines: list[str]) -> int:
    junction_boxes = parse_junction_boxes(lines)
    connections = calculate_connection_distances(junction_boxes)

    circuits: list[list[Coordinate]] = []

    while True:
        last_connection = make_smallest_connection(circuits, connections)

        if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
            break

    return last_connection[0].x * last_connection[1].x


def parse_junction_boxes(lines: list[str]) -> list[Coordinate]:
    junction_boxes: list[Coordinate] = []

    for line in lines:
        x, y, z = map(int, line.split(','))
        junction_boxes.append(Coordinate(x, y, z))

    return junction_boxes


def calculate_connection_distances(junction_boxes: list[Coordinate]) -> dict[tuple[Coordinate, Coordinate], float]:
    connections: dict[tuple[Coordinate, Coordinate], float] = {}

    for i in range(len(junction_boxes)):
        c1 = junction_boxes[i]
        for j in range(i + 1, len(junction_boxes)):
            c2 = junction_boxes[j]
            connections[(c1, c2)] = distance(c1, c2)

    return connections


def distance(loc1: Coordinate, loc2: Coordinate) -> float:
    return sqrt(((loc1.x - loc2.x) ** 2) + ((loc1.y - loc2.y) ** 2) + ((loc1.z - loc2.z) ** 2))


def make_smallest_connection(circuits: list[list[Coordinate]], connections: dict[tuple[Coordinate, Coordinate], float]) -> tuple[Coordinate, Coordinate]:
    min_key = min(connections, key=connections.get)

    increased_circuits = []
    for circuit in circuits:
        if min_key[0] in circuit:
            increased_circuits.append(circuit)
            if min_key[1] not in circuit:
                circuit.append(min_key[1])
        elif min_key[1] in circuit:
            increased_circuits.append(circuit)
            if min_key[0] not in circuit:
                circuit.append(min_key[0])

    if not increased_circuits:
        new_circuit = [min_key[0], min_key[1]]
        circuits.append(new_circuit)
    elif len(increased_circuits) > 1:
        merged_circuit = set()
        for circuit in increased_circuits:
            merged_circuit |= set(circuit)
            circuits.remove(circuit)
        circuits.append(list(merged_circuit))

    connections.pop(min_key)

    return min_key