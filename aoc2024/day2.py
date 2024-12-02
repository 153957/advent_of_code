from itertools import pairwise
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    return sum(
        (
            all(1 <= int(first) - int(second) <= 3 for first, second in pairwise(line.split()))
            or all(-3 <= int(first) - int(second) <= -1 for first, second in pairwise(line.split()))
        )
        for line in data
    )


def part2(data):
    data = [[int(value) for value in line.split()] for line in data]

    return sum(
        any(
            (
                all(1 <= first - second <= 3 for first, second in pairwise([*line[:i], *line[i + 1:]]))
                or all(-3 <= first - second <= -1 for first, second in pairwise([*line[:i], *line[i + 1:]]))
            )
            for i in range(len(line))
        )
        for line in data
    )


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
