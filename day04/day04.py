from typing import Self


type Input = Grid

NEIGHBORS = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]


def parse(filename: str) -> Input:
    with open(filename, "r") as fp:
        lines = fp.read()

    return Grid.new(lines)


def part1(input: Input) -> int:
    return find_rolls(input)


def part2(input: Input) -> int:
    removed = 1
    roll_count = 0
    while removed > 0:
        removed = find_rolls(input, remove=True)
        roll_count += removed
    return roll_count


class Grid:
    def __init__(self, height: int, width: int, data: list[list]):
        self.height = height
        self.width = width
        self.data = data

    @classmethod
    def new(cls, lines: str) -> Self:
        data = [list(line.strip()) for line in lines.splitlines()]

        return cls(height=len(data), width=len(data[0]), data=data)

    def get(self, row: int, col: int) -> str:
        return self.data[row][col]

    def delete(self, row: int, col: int):
        self.data[row][col] = "X"


def find_rolls(grid: Grid, remove: bool = False) -> int:
    rolls_removed = 0
    for row in range(grid.height):
        for col in range(grid.width):
            if grid.get(row, col) == "@":
                adjacent = 0
                for x, y in NEIGHBORS:
                    neighbor_row, neighbor_col = (row + x, col + y)
                    if (
                        0 <= neighbor_row < grid.height
                        and 0 <= neighbor_col < grid.width
                        and grid.get(neighbor_row, neighbor_col) == "@"
                    ):
                        adjacent += 1
                if adjacent < 4:
                    if remove:
                        grid.delete(row, col)
                    rolls_removed += 1
    return rolls_removed
