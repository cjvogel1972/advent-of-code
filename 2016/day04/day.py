import re
from collections import Counter, defaultdict


def solve_part1(lines: list[str]) -> int:
    result = 0
    for line in lines:
        encrypted_room_name, sector_id, checksum = parse_room(line)
        if is_real_room(encrypted_room_name, checksum):
            result += sector_id

    return result


def solve_part2(lines: list[str]) -> int:
    for line in lines:
        encrypted_room_name, sector_id, _ = parse_room(line)

        name = decrypt_name(encrypted_room_name, sector_id)
        if name.startswith("northpole"):
            return sector_id

    return 0


def parse_room(room_name: str) -> tuple[str, int, str]:
    match = re.search(r"([-a-z]+)-([0-9]+)\[([a-z]+)\]", room_name)

    return match.group(1), int(match.group(2)), match.group(3)


def is_real_room(encrypted_room_name: str, checksum: str) -> bool:
    frequencies = Counter(encrypted_room_name.replace('-', ''))

    sorted_chars = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))
    computed_checksum = "".join(c for c, _ in sorted_chars[:5])

    return checksum == computed_checksum


def decrypt_name(encrypted_name: str, sector_id: int) -> str:
    return "".join(' ' if c == '-' else chr(((ord(c) - ord('a') + sector_id) % 26) + ord('a')) for c in encrypted_name)
