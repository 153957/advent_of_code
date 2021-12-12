from .get_inputs import get_inputs


def part1(commands):
    horizontal = 0
    depth = 0

    for command in commands:
        instruction, _, units = command.partition(' ')
        units = int(units)
        if instruction == 'up':
            depth -= units
        elif instruction == 'down':
            depth += units
        elif instruction == 'forward':
            horizontal += units

    return depth * horizontal


def part2(commands):
    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        instruction, _, units = command.partition(' ')
        units = int(units)
        if instruction == 'up':
            aim -= units
        elif instruction == 'down':
            aim += units
        elif instruction == 'forward':
            horizontal += units
            depth += (aim * units)

    return depth * horizontal


if __name__ == '__main__':
    commands = get_inputs('day2.txt')
    print(part1(commands))
    print(part2(commands))

