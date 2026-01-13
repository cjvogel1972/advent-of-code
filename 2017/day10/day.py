def solve_part1(lines: list[str]) -> int:
    sparse_hash = create_sparse_hash(256, lines[0])
    return sparse_hash[0] * sparse_hash[1]


def solve_part2(lines: list[str]) -> str:
    lengths = input_to_ascii(lines[0])
    sparse_hash = create_sparse_hash(256, lengths, 64)
    dense_hash = create_dense_hash(sparse_hash)

    return ''.join(f'{item:02x}' for item in dense_hash)


def input_to_ascii(orig_key: str) -> str:
    result: list[str] = []
    for c in orig_key:
        result.append(str(ord(c)))
    result.append("17")
    result.append("31")
    result.append("73")
    result.append("47")
    result.append("23")

    return ','.join(result)


def create_sparse_hash(size: int, lengths_str: str, rounds: int = 1) -> list[int]:
    marks = [i for i in range(size)]
    lengths = list(map(int, lengths_str.split(',')))

    pos = 0
    skip = 0
    for _ in range(rounds):
        for l in lengths:
            if pos + l > size:
                section = marks[pos:] + marks[:(pos + l - size)]
                section.reverse()
                if l == size:
                    marks = section[-pos:] + section[:-pos]
                else:
                    marks = section[(size - pos):] + marks[(pos + l - size):pos] + section[:(size - pos)]
            else:
                section = marks[pos:pos + l]
                section.reverse()
                marks = marks[:pos] + section[:] + marks[pos + l:]

            pos = (pos + l + skip) % size
            skip += 1

    return marks


def create_dense_hash(marks: list[int]) -> list[int]:
    result: list[int] = []
    for i in range(16):
        block = marks[i * 16:(i + 1) * 16]
        result.append(xor_block(block))

    return result


def xor_block(block: list[int]) -> int:
    result = 0
    for b in block:
        result ^= b

    return result
