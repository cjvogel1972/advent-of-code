import re

PARSER = re.compile(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")


class Reindeer:
    def __init__(self, name, speed, flight_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.flight_duration = flight_duration
        self.rest_duration = rest_duration
        self.points = 0
        self.distance = 0
        self.flight_remaining = flight_duration
        self.rest_remaining = 0

    def next_second(self):
        if self.flight_remaining > 0:
            self.distance += self.speed
            self.flight_remaining -= 1
            if self.flight_remaining == 0:
                self.rest_remaining += self.rest_duration
        elif self.rest_remaining > 0:
            self.rest_remaining -= 1
            if self.rest_remaining == 0:
                self.flight_remaining = self.flight_duration


def solve_part1(lines: list[str]) -> int:
    max_distance = 0

    for line in lines:
        name, speed, duration, rest = PARSER.match(line).groups()
        speed = int(speed)
        duration = int(duration)
        rest = int(rest)
        distance = compute_distance(speed, duration, rest, 2503)
        max_distance = max(max_distance, distance)

    return max_distance


def solve_part2(lines: list[str]) -> int:
    reindeer = {}
    for line in lines:
        name, speed, duration, rest = PARSER.match(line).groups()
        speed = int(speed)
        duration = int(duration)
        rest = int(rest)
        reindeer[name] = Reindeer(name, speed, duration, rest)

    return compute_max_score(reindeer, 2503)


def compute_distance(speed: int, duration: int, rest: int, time: int) -> int:
    total_cycle = duration + rest
    num_cycles = time // total_cycle

    t = total_cycle * num_cycles
    more_flight_time = min(duration, time - t)

    return (speed * duration * num_cycles) + (speed * more_flight_time)


def compute_max_score(reindeer: dict[str, Reindeer], time: int) -> int:
    for t in range(time):
        max_distance = 0
        for r in reindeer.values():
            r.next_second()
            max_distance = max(max_distance, r.distance)

        for r in reindeer.values():
            if r.distance == max_distance:
                r.points += 1

    max_points = 0
    for r in reindeer.values():
        max_points = max(max_points, r.points)

    return max_points
