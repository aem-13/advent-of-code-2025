type Input = str


def parse(filename: str) -> Input:
    with open(filename, "r") as fp:
        return fp.read()


def part1(input: Input) -> int:
    lines = input.splitlines()
    splits = 0
    beam_array = [1 if char == "S" else 0 for char in lines[0]]
    for line in lines[1:]:
        for index, char in enumerate(line):
            if "^" == char and 1 == beam_array[index]:
                beam_array[index] = 0
                beam_array[index - 1] = 1
                beam_array[index + 1] = 1
                splits += 1
    return splits


def part2(input: Input) -> int:
    lines = input.splitlines()
    beam_array = [1 if char == "S" else 0 for char in lines[0]]
    for line in lines[1:]:
        for index, char in enumerate(line):
            if "^" == char and 0 < beam_array[index]:
                visits = beam_array[index]
                beam_array[index] = 0
                beam_array[index - 1] += visits
                beam_array[index + 1] += visits
    return sum(beam_array)
