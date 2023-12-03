from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    product_ids = []
    for x, line in enumerate(data):
        in_part_id = False
        for y, value in enumerate(line):
            if value.isdigit():
                if not in_part_id:
                    part_id = int(value)
                    min_y = y
                    in_part_id = True
                else:
                    part_id *= 10
                    part_id += int(value)
                if y == len(line) - 1:
                    product_ids.append((part_id, x, min_y, y - 1))
            elif in_part_id:
                product_ids.append((part_id, x, min_y, y - 1))
                in_part_id = False

    line_length = len(data[0])
    part_sum = sum(
        part_id
        for part_id, x, min_y, max_y in product_ids
        if any(
            not data[i][j].isdigit() and not data[i][j] == '.'
            for i in range(max(0, x - 1), min(len(data), x + 2))
            for j in range(max(0, min_y - 1), min(line_length, max_y + 2))
        )
    )

    return part_sum


def part2(data):
    product_ids = []
    for x, line in enumerate(data):
        in_part_id = False
        for y, value in enumerate(line):
            if value.isdigit():
                if not in_part_id:
                    part_id = int(value)
                    min_y = y
                    in_part_id = True
                else:
                    part_id *= 10
                    part_id += int(value)
                if y == len(line) - 1:
                    product_ids.append((part_id, x, min_y, y - 1))
            elif in_part_id:
                product_ids.append((part_id, x, min_y, y - 1))
                in_part_id = False

    gears = {(x, y): [] for x, line in enumerate(data) for y, value in enumerate(line) if data[x][y] == '*'}
    line_length = len(data[0])
    for part_id, x, min_y, max_y in product_ids:
        for i in range(max(0, x - 1), min(len(data), x + 2)):
            for j in range(max(0, min_y - 1), min(line_length, max_y + 2)):
                if (i, j) in gears:
                    gears[(i, j)].append(part_id)

    gear_ratio = sum(
        gear[0] * gear[1]
        for gear in gears.values()
        if len(gear) == 2
    )

    return gear_ratio


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
