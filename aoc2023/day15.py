from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    result = 0
    for segment in data[0].strip().split(','):
        hashed = 0
        for character in segment:
            hashed = (hashed + ord(character)) * 17 % 256
        result += hashed

    return result


def part2(data):
    ...


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
