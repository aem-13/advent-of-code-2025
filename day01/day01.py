def parse_input(filename: str) -> list | dict:
    with open(filename, "r") as fp:
        lines = fp.readlines()
        data = [line.strip() for line in lines]
    return data


def part1(input: list[str]) -> int:
    pw = 0
    dial = 50
    for rotation in input:
        command = int(rotation[1:])
        if rotation[0] == "L":
            command *= -1

        dial = (dial + command) % 100
        if dial == 0:
            pw += 1

    return pw


def part2(input: list[str]) -> int:
    pw = 0
    dial = 50
    for rotation in input:
        command = int(rotation[1:])
        if rotation[0] == "L":
            pw += ((100 - dial) % 100 + command) // 100
            command *= -1
        else:
            pw += (dial + command) // 100

        dial = (dial + command) % 100

    return pw
