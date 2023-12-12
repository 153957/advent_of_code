from itertools import combinations
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    result = 0

    for line in data:
        arrangement, _, groups = line.partition(' ')
        broken_counts = [int(group) for group in groups.split(',')]
        missing_broken = sum(broken_counts) - arrangement.count('#')

        unknown_positions = [i for i, mark in enumerate(arrangement) if mark == '?']

        for locations in combinations(unknown_positions, missing_broken):
            new_arrangement = list(arrangement)
            for location in locations:
                new_arrangement[location] = '#'
            new_arrangement = ''.join(new_arrangement).replace('.', ' ').replace('?', ' ')
            if [len(group) for group in new_arrangement.split()] == broken_counts:
                result += 1

    return result


def part2(data):
    raise Exception('This takes too long')

    result = 0

    for line in data:
        arrangement, _, groups = line.partition(' ')

        # unfold
        broken_counts = [int(group) for group in groups.split(',')] * 5
        arrangement = '?'.join([arrangement] * 5)

        missing_broken = sum(broken_counts) - arrangement.count('#')

        unknown_positions = [i for i, mark in enumerate(arrangement) if mark == '?']

        for locations in combinations(unknown_positions, missing_broken):
            new_arrangement = list(arrangement)
            for location in locations:
                new_arrangement[location] = '#'
            new_arrangement = ''.join(new_arrangement).replace('.', ' ').replace('?', ' ')
            if [len(group) for group in new_arrangement.split()] == broken_counts:
                result += 1

    return result


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
