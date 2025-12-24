def solve_part1(lines: list[str]) -> int:
    present_sizes: list[int] = [0] * 6
    for i in range(6):
        for j in range(3):
            present_sizes[i] += lines[(i * 5) + j + 1].count("#")

    present_fit_count = 0

    for line in lines[30:]:
        dimensions, num_presents = line.split(":")
        x_size, y_size = map(int, dimensions.split("x"))
        present_count = list(map(int, num_presents.strip().split(" ")))
        region_size = x_size * y_size

        region_present_sizes = 0
        for i, c in enumerate(present_count):
            region_present_sizes += c * present_sizes[i]

        # if the total size of all the presents is bigger than the region, they won't fit
        if region_present_sizes > region_size:
            continue

        # if we can lay them all down without manipulation, they'll all fit
        if (x_size // 3) * (y_size // 3) >= sum(present_count):
            present_fit_count += 1
            continue

        print("Need to manipulate presents")

    return present_fit_count


def solve_part2(lines: list[str]) -> int:
    return 0
