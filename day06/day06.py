type Input = str


def parse(filename: str) -> Input:
    with open(filename, "r") as fp:
        return fp.read()


def part1(input: Input) -> int:
    total = 0
    for row in zip(*[line.split() for line in input.splitlines()]):
        operator = row[-1]
        expr = operator.join(row[:-1])
        total += eval(expr)
    return total


def part2(input: Input) -> int:
    total = 0
    operands = []
    for row in zip(*[line[::-1] for line in input.splitlines()]):
        operands.append("".join(s.strip() for s in row[:-1]))
        if (operator := row[-1]) in ("*", "+"):
            expr = operator.join(operand for operand in operands if operand)
            total += eval(expr)
            operands = []
    return total
