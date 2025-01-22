def solve_part1(lines: list[str]) -> str:
    password = lines[0]

    return get_next_good_password(password)


def solve_part2(lines: list[str]) -> str:
    password = lines[0]

    password = get_next_good_password(password)

    return get_next_good_password(password)


def get_next_good_password(password):
    while True:
        password = increment_password(password)
        if is_good_password(password):
            break

    return password


def increment_password(password: str) -> str:
    new_password = ""

    for i in range(len(password) - 1, 0, -1):
        ch = password[i]
        if ch == 'z':
            ch = 'a'
            new_password = ch + new_password
        else:
            ch = chr(ord(ch) + 1)
            while not has_good_letters(ch):
                ch = chr(ord(ch) + 1)
            new_password = ch + new_password
            break

    new_password = password[:i] + new_password

    return new_password


def is_good_password(password: str) -> bool:
    if has_increasing_letters(password) and has_good_letters(password) and has_two_non_overlapping(password):
        return True

    return False


def has_increasing_letters(password: str) -> bool:
    for i in range(len(password) - 2):
        c1 = ord(password[i])
        c2 = ord(password[i + 1])
        c3 = ord(password[i + 2])

        if c1 + 1 == c2 and c2 + 1 == c3:
            return True

    return False


def has_good_letters(password: str) -> bool:
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    return True


def has_two_non_overlapping(password: str) -> bool:
    used_doubles = set()

    for a, b in zip(password, password[1:]):
        if a == b:
            used_doubles.add(a)

    return len(used_doubles) > 1
