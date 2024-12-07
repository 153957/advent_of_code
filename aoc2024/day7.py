from itertools import product
from operator import add, mul
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    total_result = 0
    for line in data:
        target_result, _, calibration = line.partition(': ')
        target_result = int(target_result)
        calibration_values = [int(calibration_value) for calibration_value in calibration.split(' ')]
        remaining_values = calibration_values[1:]
        for operators in product([add, mul], repeat=len(remaining_values)):
            current_value = calibration_values[0]
            for operator, calibration_value in zip(operators, remaining_values):
                current_value = operator(current_value, calibration_value)
            if current_value == target_result:
                total_result += target_result
                break

    return total_result


def part2(data):
    def concat(a, b):
        return int(f'{a}{b}')

    total_result = 0
    for line in data:
        target_result, _, calibration = line.partition(': ')
        target_result = int(target_result)
        calibration_values = [int(calibration_value) for calibration_value in calibration.split(' ')]
        remaining_values = calibration_values[1:]
        for operators in product([add, mul, concat], repeat=len(remaining_values)):
            current_value = calibration_values[0]
            for operator, calibration_value in zip(operators, remaining_values):
                current_value = operator(current_value, calibration_value)
            if current_value == target_result:
                total_result += target_result
                break

    return total_result


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
