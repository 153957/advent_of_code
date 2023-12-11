from itertools import combinations

from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    expansion_columns = [j for j in range(len(data[0])) if all(obs == '.' for line in data for obs in line[j])] + [len(data[0])]

    galaxies = []
    offset_row = 0
    offset_column = 0
    for x, line in enumerate(data):
        if all(obs == '.' for obs in line):
            offset_row += 1
        offset_column = 0
        for y, obs in enumerate(line):
            if y > expansion_columns[offset_column]:
                offset_column += 1
            if obs == '#':
                galaxies.append((x + offset_row, y + offset_column))

    return sum(
        abs(alpha[0] - beta[0]) + abs(alpha[1] - beta[1])
        for alpha, beta in combinations(galaxies, 2)
    )


def part2(data):
    expansion_columns = [j for j in range(len(data[0])) if all(obs == '.' for line in data for obs in line[j])] + [len(data[0])]

    expansion = 1_000_000 - 1

    galaxies = []
    offset_row = 0
    offset_column = 0
    for x, line in enumerate(data):
        if all(obs == '.' for obs in line):
            offset_row += 1
        offset_column = 0
        for y, obs in enumerate(line):
            if y == expansion_columns[offset_column]:
                offset_column += 1
            elif obs == '#':
                galaxies.append((x + (offset_row * expansion), y + (offset_column * expansion)))

    return sum(
        abs(alpha[0] - beta[0]) + abs(alpha[1] - beta[1])
        for alpha, beta in combinations(galaxies, 2)
    )


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
