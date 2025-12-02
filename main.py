from day01 import day01


def main():
    day01_path = "day01/input.txt"
    day01_input = day01.parse_input(day01_path)

    print(f"Day01, Part One: {day01.part1(day01_input)}")
    print(f"Day01, Part Two: {day01.part2(day01_input)}")


if __name__ == "__main__":
    main()
