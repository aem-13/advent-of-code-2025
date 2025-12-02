type Input = str


def parse(filename: str) -> str:
    with open(filename, "r") as fp:
        lines = fp.read()

    return lines


def part1(input: Input) -> int:
    pw = 0
    dial = 50
    for rotation in input.splitlines():
        command = int(rotation[1:])
        if rotation[0] == "L":
            command *= -1

        dial = (dial + command) % 100
        if dial == 0:
            pw += 1

    return pw


def part2(input: Input) -> int:
    pw = 0
    dial = 50
    for rotation in input.splitlines():
        command = int(rotation[1:])
        if rotation[0] == "L":
            pw += ((100 - dial) % 100 + command) // 100
            command *= -1
        else:
            pw += (dial + command) // 100

        dial = (dial + command) % 100

    return pw
