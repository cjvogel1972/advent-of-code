import hashlib


def solve_part1(lines: list[str]) -> str:
    door_id = lines[0]
    index = 0

    password = ""

    while len(password) < 8:
        index, hash = find_next_interesting_hash(door_id, index)

        password += hash[5]

    return password


def solve_part2(lines: list[str]) -> str:
    door_id = lines[0]
    index = 0

    password = {}

    while len(password) < 8:
        index, hash = find_next_interesting_hash(door_id, index)

        position = int(hash[5], 16)
        if position < 8 and position not in password:
            password[position] = hash[6]

    pw = "".join([password[i] for i in range(8)])

    return pw


def memoize(f):
    fast = {}

    def partner(door_id: str, index: int):
        if index not in fast:
            fast[index] = f(door_id, index)
        return fast[index]

    return partner


@memoize
def find_next_interesting_hash(door_id: str, index: int) -> tuple[int, str]:
    hash = ""

    while not hash.startswith("00000"):
        data = door_id + str(index)
        m = hashlib.md5(data.encode())
        hash = m.hexdigest()
        index += 1

    return index, hash
