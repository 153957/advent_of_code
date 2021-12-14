from .get_inputs import get_inputs


def part1(lines):
    encountered_once = set()
    encountered_twice = set()

    for line in lines:
        start, end = line.split(' -> ')
        start_x, start_y = [int(point) for point in start.split(',')]
        end_x, end_y = [int(point) for point in end.split(',')]

        low_x, high_x = sorted([start_x, end_x])
        low_y, high_y = sorted([start_y, end_y])

        if low_x == high_x:
            for y in range(low_y, high_y + 1):
                coordinate = (low_x, y)
                if coordinate in encountered_once:
                    encountered_twice.add(coordinate)
                encountered_once.add(coordinate)

        elif low_y == high_y:
            for x in range(low_x, high_x + 1):
                coordinate = (x, low_y)
                if coordinate in encountered_once:
                    encountered_twice.add(coordinate)
                encountered_once.add(coordinate)

    return len(encountered_twice)


def part2(lines):
    encountered_once = set()
    encountered_twice = set()

    for line in lines:
        start, end = line.split(' -> ')
        start_x, start_y = [int(point) for point in start.split(',')]
        end_x, end_y = [int(point) for point in end.split(',')]

        low_x, high_x = sorted([start_x, end_x])
        low_y, high_y = sorted([start_y, end_y])

        if low_x == high_x:
            for y in range(low_y, high_y + 1):
                coordinate = (low_x, y)
                if coordinate in encountered_once:
                    encountered_twice.add(coordinate)
                encountered_once.add(coordinate)

        elif low_y == high_y:
            for x in range(low_x, high_x + 1):
                coordinate = (x, low_y)
                if coordinate in encountered_once:
                    encountered_twice.add(coordinate)
                encountered_once.add(coordinate)

        elif (high_x - low_x) == (high_y - low_y):
            if (
                start_x < end_x and start_y < end_y
                or start_x > end_x and start_y > end_y
            ):
                for coordinate in zip(range(low_x, high_x + 1), range(low_y, high_y + 1)):
                    if coordinate in encountered_once:
                        encountered_twice.add(coordinate)
                    encountered_once.add(coordinate)
            else:
                for coordinate in zip(reversed(range(low_x, high_x + 1)), range(low_y, high_y + 1)):
                    if coordinate in encountered_once:
                        encountered_twice.add(coordinate)
                    encountered_once.add(coordinate)

    return len(encountered_twice)


if __name__ == '__main__':
    lines = get_inputs('day5.txt')
    print(part1(lines))
    print(part2(lines))

