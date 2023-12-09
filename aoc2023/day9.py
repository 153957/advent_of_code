from itertools import pairwise
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):

    def get_last_diff(history):
        derivative = [y - x for x, y in pairwise(history)]
        if len(set(derivative)) == 1:
            return derivative[-1]
        else:
            return derivative[-1] + get_last_diff(derivative)

    result = 0
    for line in data:
        history = [int(value) for value in line.split()]
        result += history[-1] + get_last_diff(history)

    return result


def part2(data):

    def get_last_diff(history):
        derivative = [y - x for x, y in pairwise(history)]
        if len(set(derivative)) == 1:
            return derivative[-1]
        else:
            return derivative[-1] + get_last_diff(derivative)

    result = 0
    for line in data:
        history = list(reversed([int(value) for value in line.split()]))
        result += history[-1] + get_last_diff(history)

    return result


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
