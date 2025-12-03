from itertools import combinations

type Input = list[tuple[int, int]]


def parse(filename: str) -> Input:
    with open(filename, "r", newline="") as fp:
        lines = fp.read()

    return from_string(lines)


def part1(input: Input) -> int:
    invalid = 0
    for begin, end in input:
        for n in range(begin, end + 1):
            s = str(n)
            half_n = len(s) // 2
            first_half = s[:half_n]
            second_half = s[half_n:]
            if first_half == second_half:
                invalid += n

    return invalid


def part2(input: Input) -> int:
    """The (s + s)[1:-1] trick is apparently well-known in formal language theory and string algorithms.
    A one-line test for string periodicity. I didn't know it
    invalid = 0
    for begin, end in input:
        for n in range(begin, end + 1):
            s = str(n)
            if s in (s + s)[1:-1]:
                invalid += n
    return invalid

    original, naive solution below
    """

    invalid = 0
    for begin, end in input:
        for n in range(begin, end + 1):
            s = str(n)
            length_n = len(s)
            subs = {s[x:y] for x, y in combinations(range(length_n + 1), r=2)}
            sub_counts = {sub: s.count(sub) for sub in subs if s.count(sub) != 1}
            for k, v in sub_counts.items():
                if k * v == s:
                    invalid += n
                    break
    return invalid


def from_string(s: str) -> Input:
    result = []
    for part in s.split(","):
        left, right = part.split("-")
        result.append((int(left), int(right)))
    return result
