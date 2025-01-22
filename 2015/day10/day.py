def solve_part1(lines: list[str]) -> int:
    number = lines[0]

    for _ in range(40):
        number = look_and_say(number)

    return len(number)


def solve_part2(lines: list[str]) -> int:
    number = lines[0]

    for _ in range(50):
        number = look_and_say(number)

    return len(number)


def look_and_say(number: str) -> str:
    i = 0
    new_number = ""
    curr_num = number[0]
    num_count = 0

    while i < len(number):
        if number[i] == curr_num:
            num_count += 1
        else:
            new_number += str(num_count) + str(curr_num)
            curr_num = number[i]
            num_count = 1
        i += 1

    new_number += str(num_count) + str(curr_num)

    return new_number