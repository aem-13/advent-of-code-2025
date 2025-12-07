import sys
from day01 import day01
from day02 import day02
from day03 import day03
from day04 import day04
from day05 import day05
from day06 import day06
from day07 import day07

DISPATCH = {
    "day01": day01,
    "day02": day02,
    "day03": day03,
    "day04": day04,
    "day05": day05,
    "day06": day06,
    "day07": day07,
}


def run():
    day = sys.argv[1]
    part = sys.argv[2]
    dispatch = DISPATCH[day]
    path = f"{day}/input.txt"
    input = dispatch.parse(path)

    if "1" == part:
        print(f"{day}, Part One: {dispatch.part1(input)}")
    elif "2" == part:
        print(f"{day}, Part Two: {dispatch.part2(input)}")


if __name__ == "__main__":
    run()
