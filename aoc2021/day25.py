from .get_inputs import get_inputs


def part1(cucumbers):
    cucumbers = [
        [cucumber for cucumber in cucumber_line]
        for cucumber_line in cucumbers
    ]

    column_length = len(cucumbers)
    line_length = len(cucumbers[0])

    iterations = 0
    moved = True

    previous = [cucumber_line[:] for cucumber_line in cucumbers]

    while moved:
        moved = False
        cucumbers = [previous_line[:] for previous_line in previous]
        # Move east
        for x in range(line_length):
            target = (x + 1) % line_length
            for y in range(column_length):
                if previous[y][x] == '>' and previous[y][target] == '.':
                    moved = True
                    cucumbers[y][x] = '.'
                    cucumbers[y][target] = '>'
        previous = [cucumber_line[:] for cucumber_line in cucumbers]

        # Move south
        for y in range(column_length):
            target = (y + 1) % column_length
            for x in range(line_length):
                if previous[y][x] == 'v' and previous[target][x] == '.':
                    moved = True
                    cucumbers[y][x] = '.'
                    cucumbers[target][x] = 'v'

        previous = [cucumber_line[:] for cucumber_line in cucumbers]
        iterations += 1

    return iterations


def part2(cucumbers):
    return ...


if __name__ == '__main__':
    cucumbers = get_inputs('day25.txt')
    print(part1(cucumbers))
    print(part2(cucumbers))
