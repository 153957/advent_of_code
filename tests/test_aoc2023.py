import unittest

from aoc2023 import get_inputs


class TestDayMixin:
    def setUp(self):
        self.day = __import__(f'aoc2023.day{self.n}', fromlist=['*'])
        self.inputs_part1 = get_inputs.get_inputs(f'day{self.n}_example.txt')
        try:
            self.inputs_part2 = get_inputs.get_inputs(f'day{self.n}_part2_example.txt')
        except FileNotFoundError:
            self.inputs_part2 = self.inputs_part1

    def test_part1(self):
        self.assertEqual(self.part1, self.day.part1(self.inputs_part1))

    def test_part2(self):
        self.assertEqual(self.part2, self.day.part2(self.inputs_part2))



class TestDay1(TestDayMixin, unittest.TestCase):
    n = 1
    part1 = 142
    part2 = 281


class TestDay2(TestDayMixin, unittest.TestCase):
    n = 2
    part1 = 8
    part2 = 2286


class TestDay3(TestDayMixin, unittest.TestCase):
    n = 3
    part1 = 4361
    part2 = 467835


class TestDay4(TestDayMixin, unittest.TestCase):
    n = 4
    part1 = 13
    part2 = 30


class TestDay5(TestDayMixin, unittest.TestCase):
    n = 5
    part1 = 35
    part2 = 46


class TestDay6(TestDayMixin, unittest.TestCase):
    n = 6
    part1 = 288
    part2 = 71503


class TestDay7(TestDayMixin, unittest.TestCase):
    n = 7
    part1 = 6440
    part2 = 5905


class TestDay8(TestDayMixin, unittest.TestCase):
    n = 8
    part1 = 6
    part2 = 6


class TestDay9(TestDayMixin, unittest.TestCase):
    n = 9
    part1 = 114
    part2 = 2


class TestDay10(TestDayMixin, unittest.TestCase):
    n = 10
    part1 = 8
    part2 = 10


class TestDay11(TestDayMixin, unittest.TestCase):
    n = 11
    part1 = 374
    part2 = 82000210


# FIXME to slow
# class TestDay12(TestDayMixin, unittest.TestCase):
#     n = 12
#     part1 = 21
#     part2 = 525152


class TestDay13(TestDayMixin, unittest.TestCase):
    n = 13
    part1 = 405
    part2 = 400


class TestDay14(TestDayMixin, unittest.TestCase):
    n = 14
    part1 = 136
    part2 = None


class TestDay15(TestDayMixin, unittest.TestCase):
    n = 15
    part1 = 1320
    part2 = None


class TestDay16(TestDayMixin, unittest.TestCase):
    n = 16
    part1 = 46
    part2 = 51

class TestDay17(TestDayMixin, unittest.TestCase):
    n = 17
    part1 = None
    part2 = None


class TestDay18(TestDayMixin, unittest.TestCase):
    n = 18
    part1 = None
    part2 = None


class TestDay19(TestDayMixin, unittest.TestCase):
    n = 19
    part1 = None
    part2 = None


class TestDay20(TestDayMixin, unittest.TestCase):
    n = 20
    part1 = None
    part2 = None


class TestDay21(TestDayMixin, unittest.TestCase):
    n = 21
    part1 = None
    part2 = None


class TestDay22(TestDayMixin, unittest.TestCase):
    n = 22
    part1 = None
    part2 = None


class TestDay23(TestDayMixin, unittest.TestCase):
    n = 23
    part1 = None
    part2 = None


class TestDay24(TestDayMixin, unittest.TestCase):
    n = 24
    part1 = None
    part2 = None


class TestDay25(TestDayMixin, unittest.TestCase):
    n = 25
    part1 = None
    part2 = None
