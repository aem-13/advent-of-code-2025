import day03

EXAMPLE = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_part1():
    assert 357 == day03.part1(EXAMPLE)


def test_part2():
    assert 3121910778619 == day03.part2(EXAMPLE)
