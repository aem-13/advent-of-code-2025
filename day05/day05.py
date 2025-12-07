type Input = tuple[list, set]


def parse(filepath: str) -> Input:
    with open(filepath, "r") as f:
        parsed = f.read()

    return transform(parsed)


def part1(input: Input) -> int:
    fresh = 0
    ranges, ids = input
    for i in ids:
        for low, high in ranges:
            if low <= i <= high:
                fresh += 1
                break
    return fresh


def part2(input: Input) -> int:
    fresh = 0
    ranges, _ = input
    for low, high in ranges:
        fresh += (high + 1) - low
    return fresh


def transform(parsed: str) -> Input:
    extrema = []
    ids = set()
    for line in parsed.splitlines():
        if not line:
            continue
        if "-" in line:
            low, high = line.split("-")
            extrema.append((int(low), int(high)))
        else:
            ids.add(int(line))

    return _merge(extrema), ids


def _merge(array: list[tuple]) -> list:
    array.sort()
    ranges = [array[0]]
    for current in array[1:]:
        low, high = ranges[-1]
        if current[0] < high + 1:
            ranges[-1] = (low, max(current[1], high))
        else:
            ranges.append(current)

    return ranges
