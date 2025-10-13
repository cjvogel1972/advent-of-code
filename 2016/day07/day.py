import re


def solve_part1(lines: list[str]) -> int:
    return sum(1 for line in lines if supports_tls(line))


def solve_part2(lines: list[str]) -> int:
    return sum(1 for line in lines if supports_ssl(line))


def parse_ip(ip: str) -> tuple[list[str], list[str]]:
    regex = r"([a-z]+)(?:\[([a-z]+)\])?"
    matches = re.findall(regex, ip)

    outside_brackets = [m[0] for m in matches]
    inside_brackets = [m[1] for m in matches if m[1]]

    return outside_brackets, inside_brackets


def has_abba(s: str) -> bool:
    for i in range(len(s) - 3):
        if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
            return True

    return False


def supports_tls(line: str) -> bool:
    outside, inside = parse_ip(line)

    return any(has_abba(s) for s in outside) and not any(has_abba(s) for s in inside)


def find_aba(s: str) -> list[str]:
    return [s[i:i + 3] for i in range(len(s) - 2) if s[i] == s[i + 2] and s[i] != s[i + 1]]


def supports_ssl(line: str) -> bool:
    outside, inside = parse_ip(line)

    aba_sequences = [aba for s in outside for aba in find_aba(s)]
    bab_patterns = {aba[1] + aba[0] + aba[1] for aba in aba_sequences}

    return any(any(bab in s for bab in bab_patterns) for s in inside)
