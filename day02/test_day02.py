import day02

EXAMPLE = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def test_part1():
    test_input = day02.from_string(EXAMPLE)
    assert 1227775554 == day02.part1(test_input)


def test_part2():
    test_input = day02.from_string(EXAMPLE)
    assert 4174379265 == day02.part2(test_input)
