from collections import defaultdict


def solve_part1(lines: list[str]) -> int:
    edges = parse_edges(lines)

    return count_paths(edges, "you", "out")


def solve_part2(lines: list[str]) -> int:
    edges = parse_edges(lines)

    # since the paths are acyclic, either dac->fft or fft->dac will be 0, so we don't have to worry about duplicates
    return (count_paths(edges, "svr", "dac") * count_paths(edges, "dac", "fft") * count_paths(edges, "fft", "out")) + (
                count_paths(edges, "svr", "fft") * count_paths(edges, "fft", "dac") * count_paths(edges, "dac", "out"))


def parse_edges(lines: list[str]) -> dict[str, list[str]]:
    edges: dict[str, list[str]] = defaultdict(list[str])

    for line in lines:
        device_name = line[:3]
        outputs = line[4:].split()
        edges[device_name] = outputs

    return edges


# implements a DFS algorithm
def count_paths_from_node(current_node, dest, edges, memo):
    if current_node == dest:
        return 1

    if memo[current_node] != -1:
        return memo[current_node]

    count = 0
    for next_node in edges[current_node]:
        count += count_paths_from_node(next_node, dest, edges, memo)

    memo[current_node] = count
    return count


def count_paths(edges, src, dest):
    memo = defaultdict(lambda: -1)
    return count_paths_from_node(src, dest, edges, memo)
