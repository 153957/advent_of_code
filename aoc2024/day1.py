from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    first = sorted(int(line.split()[0]) for line in data)
    second = sorted(int(line.split()[1]) for line in data)
    return sum(abs(j - i) for i, j in zip(first, second))


def part2(data):
    first = sorted(int(line.split()[0]) for line in data)
    second = sorted(int(line.split()[1]) for line in data)
    return sum(value * second.count(value) for value in first)


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
