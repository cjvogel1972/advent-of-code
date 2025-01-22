import hashlib


def solve_part1(lines: list[str]) -> int:
    return find_key_number(lines[0], '00000')


def solve_part2(lines: list[str]) -> int:
    return find_key_number(lines[0], '000000')


def find_key_number(key: str, hash_prefix: str) -> int:
    prefix_size = len(hash_prefix)

    i = 1
    while True:
        data = key + str(i)
        hasher = hashlib.md5()
        hasher.update(data.encode())
        result = hasher.hexdigest()
        if result[:prefix_size] == hash_prefix:
            break
        i += 1

    return i
