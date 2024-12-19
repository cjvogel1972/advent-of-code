def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        l, w, h = map(int, line.split("x"))
        lxw = l * w
        wxh = w * h
        hxl = h * l
        slack = min(lxw, wxh, hxl)

        paper = 2 * lxw + 2 * wxh + 2 * hxl + slack

        total += paper

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        l, w, h = map(int, line.split("x"))
        lw = l + w
        wh = w + h
        hl = h + l
        perimeter = min(lw, wh, hl)

        ribbon = (2 * perimeter) + (l * w * h)

        total += ribbon

    return total
