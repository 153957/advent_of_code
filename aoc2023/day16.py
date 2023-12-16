import sys

from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    def next_coordinates(x, y, direction):
        match direction:
            case 'up':
                return x - 1, y, direction
            case 'down':
                return x + 1, y, direction
            case 'right':
                return x, y + 1, direction
            case 'left':
                return x, y - 1, direction

    def propogate(x, y, direction):
        if (x, y, direction) in seen:
            return

        seen.add((x, y, direction))

        if x < 0 or y < 0:
            return

        try:
            value = data[x][y]
        except IndexError:
            return

        energized[x][y] = True

        match (value, direction):
            case ('.', _) | ('|', ('up' | 'down')) | ('-', ('left' | 'right')):
                propogate(*next_coordinates(x, y, direction))
            case ('-', ('up' | 'down')):
                propogate(*next_coordinates(x, y, 'left'))
                propogate(*next_coordinates(x, y, 'right'))
            case ('|', ('left' | 'right')):
                propogate(*next_coordinates(x, y, 'up'))
                propogate(*next_coordinates(x, y, 'down'))
            case ('/', 'up'):
                propogate(*next_coordinates(x, y, 'right'))
            case ('/', 'down'):
                propogate(*next_coordinates(x, y, 'left'))
            case ('/', 'right'):
                propogate(*next_coordinates(x, y, 'up'))
            case ('/', 'left'):
                propogate(*next_coordinates(x, y, 'down'))
            case ('\\', 'up'):
                propogate(*next_coordinates(x, y, 'left'))
            case ('\\', 'down'):
                propogate(*next_coordinates(x, y, 'right'))
            case ('\\', 'right'):
                propogate(*next_coordinates(x, y, 'down'))
            case ('\\', 'left'):
                propogate(*next_coordinates(x, y, 'up'))

    sys.setrecursionlimit(10000)
    energized = [[False] * len(line) for line in data]
    seen = set()
    propogate(0, 0, 'right')

    return sum(sum(energized_line) for energized_line in energized)


def part2(data):
    sys.setrecursionlimit(10000)
    energized = [[False] * len(line) for line in data]
    seen = set()

    def next_coordinates(x, y, direction):
        match direction:
            case 'up':
                return x - 1, y, direction
            case 'down':
                return x + 1, y, direction
            case 'right':
                return x, y + 1, direction
            case 'left':
                return x, y - 1, direction

    def propogate(x, y, direction):
        if (x, y, direction) in seen:
            return

        seen.add((x, y, direction))

        if x < 0 or y < 0:
            return

        try:
            value = data[x][y]
        except IndexError:
            return

        energized[x][y] = True

        match (value, direction):
            case ('.', _) | ('|', ('up' | 'down')) | ('-', ('left' | 'right')):
                propogate(*next_coordinates(x, y, direction))
            case ('-', ('up' | 'down')):
                propogate(*next_coordinates(x, y, 'left'))
                propogate(*next_coordinates(x, y, 'right'))
            case ('|', ('left' | 'right')):
                propogate(*next_coordinates(x, y, 'up'))
                propogate(*next_coordinates(x, y, 'down'))
            case ('/', 'up'):
                propogate(*next_coordinates(x, y, 'right'))
            case ('/', 'down'):
                propogate(*next_coordinates(x, y, 'left'))
            case ('/', 'right'):
                propogate(*next_coordinates(x, y, 'up'))
            case ('/', 'left'):
                propogate(*next_coordinates(x, y, 'down'))
            case ('\\', 'up'):
                propogate(*next_coordinates(x, y, 'left'))
            case ('\\', 'down'):
                propogate(*next_coordinates(x, y, 'right'))
            case ('\\', 'right'):
                propogate(*next_coordinates(x, y, 'down'))
            case ('\\', 'left'):
                propogate(*next_coordinates(x, y, 'up'))

    sys.setrecursionlimit(10000)

    best_energy = 0
    for direction, x in ('up', len(data) - 1), ('down', 0):
        for y in range(len(data[0])):
            energized = [[False] * len(line) for line in data]
            seen = set()
            propogate(x, y, direction)
            best_energy = max(best_energy, sum(sum(energized_line) for energized_line in energized))

    for direction, y in ('right', 0), ('left', len(data[0]) - 1):
        for x in range(len(data)):
            energized = [[False] * len(line) for line in data]
            seen = set()
            propogate(x, y, direction)
            best_energy = max(best_energy, sum(sum(energized_line) for energized_line in energized))

    return best_energy


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
