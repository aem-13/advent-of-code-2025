import sys
from day01 import day01
from day02 import day02
from day03 import day03

DISPATCH = {"day01": day01, "day02": day02, "day03": day03}


def run():
    day = sys.argv[1]
    dispatch = DISPATCH[day]
    path = f"{day}/input.txt"
    input = dispatch.parse(path)

    print(f"{day}, Part One: {dispatch.part1(input)}")
    print(f"{day}, Part Two: {dispatch.part2(input)}")


if __name__ == "__main__":
    run()
