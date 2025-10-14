import re
from collections import defaultdict, deque


def solve_part1(lines: list[str]) -> int:
    return find_bot_with_chips(lines, [17, 61])


def solve_part2(lines: list[str]) -> int:
    bots, rules = parse_instructions(lines)

    instruction_queue = create_initial_instruction_queue(bots)
    outputs = {}

    while instruction_queue:
        current_bot = instruction_queue.popleft()
        process_bot_instruction(bots, current_bot, instruction_queue, outputs, rules)
        bots[current_bot] = []

    return outputs[0] * outputs[1] * outputs[2]


def find_bot_with_chips(lines: list[str], expected_chips: list[int]) -> int | None:
    bots, rules = parse_instructions(lines)

    instruction_queue = create_initial_instruction_queue(bots)
    outputs = {}

    responsible_bot = None

    while instruction_queue:
        current_bot = instruction_queue.popleft()
        chips = sorted(bots[current_bot])
        if chips[0] == expected_chips[0] and chips[1] == expected_chips[1]:
            responsible_bot = current_bot
            break

        process_bot_instruction(bots, current_bot, instruction_queue, outputs, rules)
        bots[current_bot] = []

    return responsible_bot


def parse_instructions(lines: list[str]) -> tuple[defaultdict[int, list[int]], dict[int, tuple[str, int, str, int]]]:
    bots = defaultdict(list)
    rules = dict()

    for line in lines:
        if line.startswith('value'):
            match = re.match(r'value (\d+) goes to bot (\d+)', line)
            value, bot = map(int, match.groups())
            bots[bot].append(value)
        else:
            match = re.match(r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', line)
            bot = int(match.group(1))
            low_dest, low_num = match.group(2), int(match.group(3))
            high_dest, high_num = match.group(4), int(match.group(5))
            rules[bot] = (low_dest, low_num, high_dest, high_num)

    return bots, rules


def create_initial_instruction_queue(bots: defaultdict[int, list[int]]) -> deque[int]:
    instruction_queue = deque()

    for bot, values in bots.items():
        if len(values) == 2:
            instruction_queue.append(bot)

    return instruction_queue


def process_bot_instruction(bots: defaultdict[int, list[int]], current_bot: int, instruction_queue: deque[int],
                            outputs: dict[int, int], rules: dict[int, tuple[str, int, str, int]]):
    chips = sorted(bots[current_bot])

    low_dest, low_num, high_dest, high_num = rules[current_bot]

    if low_dest == 'bot':
        bots[low_num].append(chips[0])
        if len(bots[low_num]) == 2:
            instruction_queue.append(low_num)
    elif low_dest == 'output':
        outputs[low_num] = chips[0]

    if high_dest == 'bot':
        bots[high_num].append(chips[1])
        if len(bots[high_num]) == 2:
            instruction_queue.append(high_num)
    elif high_dest == 'output':
        outputs[high_num] = chips[1]