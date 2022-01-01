import unittest

from aoc2021 import day2, day3, get_inputs


class TestDayMixin:
    def setUp(self):
        self.day = __import__(f'aoc2021.day{self.n}', fromlist=['*'])
        self.inputs = get_inputs.get_inputs(f'day{self.n}_example.txt')

    def test_part1(self):
        self.assertEqual(self.part1, self.day.part1(self.inputs))

    def test_part2(self):
        self.assertEqual(self.part2, self.day.part2(self.inputs))



class TestDay1(TestDayMixin, unittest.TestCase):
    n = 1
    part1 = 7
    part2 = 5


class TestDay2(TestDayMixin, unittest.TestCase):
    n = 2
    part1 = 150
    part2 = 900


class TestDay3(TestDayMixin, unittest.TestCase):
    n = 3
    part1 = 198
    part2 = 230


class TestDay4(TestDayMixin, unittest.TestCase):
    n = 4
    part1 = 4512
    part2 = 1924


class TestDay5(TestDayMixin, unittest.TestCase):
    n = 5
    part1 = 5
    part2 = 12


class TestDay6(TestDayMixin, unittest.TestCase):
    n = 6
    part1 = 5934
    part2 = 26984457539


class TestDay7(TestDayMixin, unittest.TestCase):
    n = 7
    part1 = 37
    part2 = 168


class TestDay8(TestDayMixin, unittest.TestCase):
    n = 8
    part1 = 26
    part2 = 61229


class TestDay9(TestDayMixin, unittest.TestCase):
    n = 9
    part1 = 15
    part2 = 1134


class TestDay10(TestDayMixin, unittest.TestCase):
    n = 10
    part1 = 26397
    part2 = 288957


class TestDay25(TestDayMixin, unittest.TestCase):
    n = 25
    part1 = 58
    part2 = ...
