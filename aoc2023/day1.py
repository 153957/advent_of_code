import string

from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    return sum(
        int(f'{next(digit for digit in calibration_value if digit in string.digits)}{next(digit for digit in calibration_value[::-1] if digit in string.digits)}')
        for calibration_value in data
    )


def part2(data):
    data = [
        calibration_value
        .replace('one', 'o1e')
        .replace('two', 't2o')
        .replace('three', 't3e')
        .replace('four', '4')
        .replace('five', '5e')
        .replace('six', '6')
        .replace('seven', '7n')
        .replace('eight', 'e8t')
        .replace('nine', 'n9e')
        for calibration_value in data
    ]

    return part1(data)


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
