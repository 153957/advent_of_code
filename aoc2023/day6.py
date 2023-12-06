from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    durations = [int(duration) for duration in data[0].partition(':')[2].split()]
    distances = [int(distance) for distance in data[1].partition(':')[2].split()]

    result = 1
    for duration, best_distance in zip(durations, distances):
        margin = 0
        for possible_time in range(duration):
            if possible_time * (duration - possible_time) > best_distance:
                margin += 1
        result *= margin

    return result


def part2(data):
    duration = int(data[0].partition(':')[2].replace(' ', ''))
    best_distance = int(data[1].partition(':')[2].replace(' ', ''))

    result = 1
    margin = 0
    for possible_time in range(duration):
        if possible_time * (duration - possible_time) > best_distance:
            margin += 1
    result *= margin

    return result


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
