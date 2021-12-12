from .get_inputs import get_inputs


def part1(measurements):
    return sum(
        True
        for previous_measurement, current_measurement in zip(measurements, measurements[1:])
        if int(previous_measurement) < int(current_measurement)
    )


def part2(measurements):
    return sum(
        True
        for previous_measurement, current_measurement in zip(measurements, measurements[3:])
        if int(previous_measurement) < int(current_measurement)
    )


if __name__ == '__main__':
    measurements = get_inputs('day1.txt')
    print(part1(measurements))
    print(part2(measurements))
