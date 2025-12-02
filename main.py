from day01 import day01
from day02 import day02


def main():
    day01_path = "day01/input.txt"
    day01_input = day01.parse(day01_path)

    print(f"Day01, Part One: {day01.part1(day01_input)}")
    print(f"Day01, Part Two: {day01.part2(day01_input)}")

    day02_path = "day02/input.txt"
    day02_input = day02.parse(day02_path)

    print(f"Day02, Part One: {day02.part1(day02_input)}")
    print(f"Day02, Part Two: {day02.part2(day02_input)}")


if __name__ == "__main__":
    main()
