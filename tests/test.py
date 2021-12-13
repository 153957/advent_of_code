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
