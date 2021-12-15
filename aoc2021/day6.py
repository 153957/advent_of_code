from .get_inputs import get_inputs


def part1(ages):
    ages = [int(age) for age in ages[0].split(',')]
    timers = [0, 0, 0, 0, 0, 0, 0]
    new = [0, 0, 0, 0, 0, 0, 0]

    for age in ages:
        timers[age] += 1

    for day in range(80):
        new[(day + 2) % 7] += timers[day % 7]
        timers[day % 7] += new[day % 7]
        new[day % 7] = 0

    return sum(fish for fish in [*timers, *new])


def part2(ages):
    ages = [int(age) for age in ages[0].split(',')]
    timers = [0, 0, 0, 0, 0, 0, 0]
    new = [0, 0, 0, 0, 0, 0, 0]

    for age in ages:
        timers[age] += 1

    for day in range(256):
        new[(day + 2) % 7] += timers[day % 7]
        timers[day % 7] += new[day % 7]
        new[day % 7] = 0

    return sum(fish for fish in [*timers, *new])


if __name__ == '__main__':
    ages = get_inputs('day6.txt')
    print(part1(ages))
    print(part2(ages))
