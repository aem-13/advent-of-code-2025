type Input = str


def parse(filename: str):
    with open(filename, "r") as fp:
        lines = fp.read()

    return lines


def part1(input: Input) -> int:
    joltage = 0
    for line in input.splitlines():
        batteries = [int(v) for v in line]
        left = 0
        left_index = 1
        for index, battery in enumerate(batteries[:-1]):
            if battery > left:
                left = battery
                left_index = index + 1
        right = max(batteries[left_index:])

        joltage += int(str(left) + str(right))

    return joltage


def part2(input: Input) -> int:
    joltage = 0
    for line in input.splitlines():
        batteries = [int(v) for v in line]
        stack = []
        budget = len(batteries) - 12
        for battery in batteries:
            while stack and stack[-1] < battery and budget > 0:
                stack.pop()
                budget -= 1
            stack.append(battery)
        stack = stack[:12]
        joltage += int("".join([str(v) for v in stack]))

    return joltage
