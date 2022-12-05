from .get_inputs import get_inputs


def part1(calories):
    return max(
        sum(int(carried_calorie) for carried_calorie in carried_calories.splitlines())
        for carried_calories in '\n'.join(calories).split('\n\n')
    )


def part2(calories):
    return sum(
        sorted(
            sum(int(carried_calorie) for carried_calorie in carried_calories.splitlines())
            for carried_calories in '\n'.join(calories).split('\n\n')
        )[-3:]
    )


if __name__ == '__main__':
    measurements = get_inputs('day1.txt')
    print(part1(measurements))
    print(part2(measurements))
