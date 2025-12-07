import day06

EXAMPLE = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


def test_part1():
    assert 4277556 == day06.part1(EXAMPLE)


def test_part2():
    assert 3263827 == day06.part2(EXAMPLE)
