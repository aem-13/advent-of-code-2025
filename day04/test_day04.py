import day04

EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_part1() -> int:
    grid = day04.Grid.new(EXAMPLE)
    assert 13 == day04.part1(grid)


def test_part2() -> int:
    grid = day04.Grid.new(EXAMPLE)
    assert 43 == day04.part2(grid)
