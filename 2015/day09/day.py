import itertools
import re

PARSER = re.compile(r"(\w+) to (\w+) = (\d+)")

def solve_part1(lines: list[str]) -> int:
    distances, locations = parse_input(lines)

    min_dist = float('inf')
    possible_routes = list(itertools.permutations(locations))

    for route in possible_routes:
        dist = 0
        for a, b  in zip(route, route[1:]):
            dist += distances[(a, b)]

        min_dist = min(min_dist, dist)

    return min_dist


def solve_part2(lines: list[str]) -> int:
    distances, locations = parse_input(lines)

    max_dist = 0
    possible_routes = list(itertools.permutations(locations))

    for route in possible_routes:
        dist = 0
        for a, b in zip(route, route[1:]):
            dist += distances[(a, b)]

        max_dist = max(max_dist, dist)

    return max_dist


def parse_input(lines):
    locations = set()
    distances = {}
    
    for line in lines:
        loc1, loc2, dist = PARSER.search(line).groups()
        dist = int(dist)
        locations.add(loc1)
        locations.add(loc2)
        distances[(loc1, loc2)] = dist
        distances[(loc2, loc1)] = dist

    return distances, locations
