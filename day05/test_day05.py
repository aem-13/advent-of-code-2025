import day05

EXAMPLE = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part1():
    assert 3 == day05.part1(day05.transform(EXAMPLE))


def test_part2():
    assert 14 == day05.part2(day05.transform(EXAMPLE))
