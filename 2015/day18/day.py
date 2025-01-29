from util.grid import directions, good_square_tuple
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    lights = [[l for l in line] for line in lines]

    lights = animate(lights, 100, False)
    return count_lights_on(lights)


def solve_part2(lines: list[str]) -> int:
    lights = [[l for l in line] for line in lines]
    width = len(lights[0])
    height = len(lights)
    lights[0][0] = lights[0][width - 1] = lights[height - 1][0] = lights[height - 1][width - 1] = '#'

    lights = animate(lights, 100, True)
    return count_lights_on(lights)


def count_lights_on(lights: list[list[str]]) -> int:
    return sum(lights[y].count("#") for y in range(len(lights)))


def animate(lights: list[list[str]], num_steps: int, stuck_lights: bool) -> list[list[str]]:
    result = lights
    for _ in range(num_steps):
        result = next_step(result, stuck_lights)

    return result


def next_step(lights: list[list[str]], stuck_lights: bool) -> list[list[str]]:
    new_lights_state = []
    width = len(lights[0])
    height = len(lights)

    for y in range(len(lights)):
        new_row = []
        for x in range(len(lights[0])):
            if stuck_lights and (y, x) in [(0, 0), (0, width - 1), (height - 1, 0), (height - 1, width - 1)]:
                new_row.append("#")
                continue

            neighbors_on = count_neighbors_on(lights, (y, x))
            if (lights[y][x] == '#' and neighbors_on in [2, 3]) or (lights[y][x] == '.' and neighbors_on == 3):
                new_row.append("#")
            else:
                new_row.append('.')
        new_lights_state.append(new_row)

    return new_lights_state


def count_neighbors_on(lights: list[list[str]], loc: tuple[int, int]) -> int:
    count = 0

    for d in directions:
        new_loc = tuple_add(loc, d)
        if good_square_tuple(lights, new_loc) and lights[new_loc[0]][new_loc[1]] == '#':
            count += 1

    return count
