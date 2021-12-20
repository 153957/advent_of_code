from .get_inputs import get_inputs


def part1(floor):
    floor = [
        [int(height) for height in line]
        for line in floor
    ]
    risk = 0

    for x in range(len(floor)):
        for y in range(len(floor[0])):
            height = floor[x][y]
            neighbors = [
                floor[x + 1][y] if x < len(floor) - 1 else 10,
                floor[x - 1][y] if x > 0 else 10,
                floor[x][y + 1] if y < len(floor[0]) - 1 else 10,
                floor[x][y - 1] if y > 0 else 10,
            ]
            if all(height < neighbor for neighbor in neighbors):
                risk += 1 + height

    return risk


def part2(floor):
    floor = [
        [int(height) != 9 for height in line]
        for line in floor
    ]
    basins = []

    for x in range(len(floor)):
        basin = set()
        for y in range(len(floor[0])):
            if floor[x][y]:
                basin.add((x, y))
            elif basin:
                basins.append(basin)
                basin = set()
        if basin:
            basins.append(basin)

    for y in range(len(floor[0])):
        basin = set()
        for x in range(len(floor)):
            if floor[x][y]:
                basin.add((x, y))
            elif basin:
                basins.append(basin)
                basin = set()
        if basin:
            basins.append(basin)

    for basin in basins:
        for other_basin in basins:
            if basin.intersection(other_basin):
                other_basin.update(basin)

    basins = {frozenset(basin) for basin in basins}

    ordered_basins = sorted(basins, key=len, reverse=True)
    size = len(ordered_basins[0]) * len(ordered_basins[1]) * len(ordered_basins[2])

    return size


if __name__ == '__main__':
    floor = get_inputs('day9.txt')
    print(part1(floor))
    print(part2(floor))
