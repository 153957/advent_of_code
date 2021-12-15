from .get_inputs import get_inputs


def part1(positions):
    positions = sorted(int(position) for position in positions[0].split(','))

    return min(
        sum(abs(position - final_position) for position in positions)
        for final_position in range(positions[0], positions[-1])
    )


def part2(positions):
    positions = sorted(int(position) for position in positions[0].split(','))

    return min(
        sum(abs(position - final_position) * (abs(position - final_position) + 1) // 2 for position in positions)
        for final_position in range(positions[0], positions[-1])
    )


if __name__ == '__main__':
    positions = get_inputs('day7.txt')
    print(part1(positions))
    print(part2(positions))
