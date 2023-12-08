from itertools import cycle
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    directions = list(0 if direction == 'L' else 1 for direction in data[0])

    mapping = {
        line.partition(' = ')[0]: (
            line.partition('(')[2].partition(',')[0],
            line.partition(', ')[2].partition(')')[0],
        )
        for line in data[2:]
    }

    location = 'AAA'

    for step, direction in enumerate(cycle(directions)):
        if location != 'ZZZ':
            location = mapping[location][direction]
        else:
            return step


def part2(data):
    directions = list(0 if direction == 'L' else 1 for direction in data[0])

    mapping = {
        line.partition(' = ')[0]: (
            line.partition('(')[2].partition(',')[0],
            line.partition(', ')[2].partition(')')[0],
        )
        for line in data[2:]
    }

    locations = [location for location in mapping if location.endswith('A')]
    first_z = [0] * len(locations)
    cycle_z = [0] * len(locations)

    for step, direction in enumerate(cycle(directions)):
        for i, location in enumerate(locations):
            if location.endswith('Z'):
                if first_z[i] == 0:
                    first_z[i] = step
                elif cycle_z[i] == 0:
                    cycle_z[i] = step - first_z[i]
        locations = [mapping[location][direction] for location in locations]
        if all(cycle_steps != 0 for cycle_steps in cycle_z):
            if first_z != cycle_z:
                raise NotImplementedError('Unsupported non-repeating loops')
            break

    largest_cycle = max(first_z)
    matching_cycles = largest_cycle

    while True:
        if all(matching_cycles % cycle_steps == 0 for cycle_steps in first_z):
            return matching_cycles
        matching_cycles += largest_cycle


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
