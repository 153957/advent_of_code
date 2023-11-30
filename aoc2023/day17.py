from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    ...


def part2(data):
    ...


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
